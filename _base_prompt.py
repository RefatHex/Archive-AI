import json


EXAMPLE_PROMPT="""
{
  "events": [
    {
      "id": 1,
      "title": "example",
      "date": "example",
      "description": "example",
      "location": "example",
      "wiki_link": "example"
    },
    {
      "id": 2,
      "title": "example",
      "date": "example",
      "description": "example",
      "location": "example",
      "wiki_link": "example"
    },
    {
      "id": 3,
      "title": "example",
      "date": "example",
      "description": "example",
      "location": "example",
      "wiki_link": "example"
    },
    {
      "id": 4,
      "title": "example",
      "date": "example",
      "description": "example",
      "location": "example",
      "wiki_link": "example"
    },
    {
      "id": 5,
      "title": "example",
      "date": "example",
      "description": "example",
      "location": "example",
      "wiki_link": "example"
    }
  ]
}"""

def get_prompt(date):
  prompt=f"Tell me all historical events on this date {date} and Please provide a response in a structured JSON format that matches the following model:\n\n{EXAMPLE_PROMPT}"
  return prompt
    