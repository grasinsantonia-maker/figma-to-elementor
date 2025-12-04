#!/usr/bin/env python3
"""
Monday.com Board Connector
IMPORTANT: Only access board ID 18390970202 - Claude's Knowledge Base
"""

import requests
import json

MONDAY_API_URL = "https://api.monday.com/v2"
MONDAY_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjU4ODI0NTA0NiwiYWFpIjoxMSwidWlkIjoyNTM1MzgxMywiaWFkIjoiMjAyNS0xMS0xOVQxMTozODo1NS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTAxOTA3MDQsInJnbiI6InVzZTEifQ.qXS9DcSunVGdoHs4wh5fBzvaPbTdKDgSsol-i3URqCU"
BOARD_ID = "18390970202"  # ONLY THIS BOARD - Claude's Knowledge Base

headers = {
    "Authorization": MONDAY_API_KEY,
    "Content-Type": "application/json"
}

def get_board_info():
    """Get board structure and columns"""
    query = f'''
    {{
        boards(ids: {BOARD_ID}) {{
            name
            columns {{
                id
                title
                type
            }}
        }}
    }}
    '''
    response = requests.post(MONDAY_API_URL, headers=headers, json={"query": query})
    return response.json()

def add_item(item_name, column_values=None):
    """Add an item to the board"""
    if column_values:
        col_values_str = json.dumps(json.dumps(column_values))
        query = f'''
        mutation {{
            create_item(
                board_id: {BOARD_ID},
                item_name: "{item_name}",
                column_values: {col_values_str}
            ) {{
                id
            }}
        }}
        '''
    else:
        query = f'''
        mutation {{
            create_item(
                board_id: {BOARD_ID},
                item_name: "{item_name}"
            ) {{
                id
            }}
        }}
        '''
    response = requests.post(MONDAY_API_URL, headers=headers, json={"query": query})
    return response.json()

def get_items():
    """Get all items from the board"""
    query = f'''
    {{
        boards(ids: {BOARD_ID}) {{
            items_page {{
                items {{
                    id
                    name
                    column_values {{
                        id
                        text
                    }}
                }}
            }}
        }}
    }}
    '''
    response = requests.post(MONDAY_API_URL, headers=headers, json={"query": query})
    return response.json()

if __name__ == "__main__":
    print("Checking Monday.com board access...")
    result = get_board_info()

    if "data" in result and result["data"]["boards"]:
        board = result["data"]["boards"][0]
        print(f"✓ Connected to board: {board['name']}")
        print(f"\nColumns:")
        for col in board["columns"]:
            print(f"  - {col['title']} (id: {col['id']}, type: {col['type']})")
    else:
        print(f"Error: {result}")
