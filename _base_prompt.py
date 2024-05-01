

EXAMPLE_PROMPT="""
Make sure to give the result in this formate.
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
}

"""

def get_prompt(date):
    prompt=f"Tell me all historical event on this date {date}  and return the result in json format as the example."+EXAMPLE_PROMPT

    print(prompt)
    
get_prompt("1967")