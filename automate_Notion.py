---
#Project Name: Automate Notion
#Author: Priya Mondal
---

#Modules Used: notion , Command: pip install notion

from notion.client import NotionClient

#Authentication Token needed. Place it.
token = ''

client =NotionClient(token_v2= token)

# Place the Tracker URL
tracker_url = ''

collection_view = client.get_collection(tracker_url)

#Sample Case -> Adding a new row into HABIT TRACKER template
newRow = collection_view.collection.add_row()

#Lets Automate our Notion
newRow.running = True
newRow.Journaling = True
newRow.screen_time_minutes = 30

