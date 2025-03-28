import os
from azure.cosmos import CosmosClient, exceptions

client = CosmosClient(os.getenv("COSMOS_URI"), os.getenv("COSMOS_KEY"))
database = client.get_database_client("BumpBitesDB")

def insert_user(id, preferences, aversions, name, weeks_pregnant):
  try:
    container = database.get_container_client("Users")
    # Check if user already exists
    existing_user = container.query_items(
        query="SELECT * FROM c WHERE c.user_id = @id",
        parameters=[{"name": "@id", "value": id}],
        enable_cross_partition_query=True
    )
    if len(list(existing_user)) > 0:
        raise ValueError(f'User with id {id} already exists.')

    # Insert user into Cosmos DB
    user_data = { 
      "id": id,
      "name": name,
      "preferences": preferences,
      "aversions": aversions,
      "weeks_pregnant": weeks_pregnant,
    }
    container.create_item(body=user_data)
    return "Successfully inserted user"
  except exceptions.CosmosHttpResponseError as e:
    raise ValueError(f"Cosmos DB error: {e.message}")
  except Exception as e:
    raise ValueError(f"An error occurred: {str(e)}")

