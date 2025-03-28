import os
from azure.cosmos import CosmosClient, exceptions
import uuid

client = CosmosClient(os.getenv("COSMOS_URI"), os.getenv("COSMOS_KEY"))
database = client.get_database_client("BumpBitesDB")

def insert_user(preferences, aversions, name, weeks_pregnant):
  try:
    container = database.get_container_client("Users")
    # Insert user into Cosmos DB
    user_data = { 
      "id": str(uuid.uuid4()),
      "name": name,
      "preferences": preferences,
      "aversions": aversions,
      "weeks_pregnant": weeks_pregnant,
    }
    container.create_item(body=user_data)
    return user_data
  except exceptions.CosmosHttpResponseError as e:
    raise ValueError(f"Cosmos DB error: {e.message}")
  except Exception as e:
    raise ValueError(f"An error occurred: {str(e)}")

def get_user(user_id):
  try:
    container = database.get_container_client("Users")
    user = container.query_items(
        query="SELECT * FROM c WHERE c.id = @id",
        parameters=[{"name": "@id", "value": user_id}],
        enable_cross_partition_query=True
    )
    return list(user)[0] if user else None
  except exceptions.CosmosHttpResponseError as e:
    raise ValueError(f"Cosmos DB error: {e.message}")
  except Exception as e:
    raise ValueError(f"An error occurred: {str(e)}")
