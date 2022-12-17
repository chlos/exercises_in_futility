gifts for nephews
___________________________________

3 2         
5 4
6 3


# 5 5
! 6 2
! 7 3


0 3 5 6
0 0 
3 1
5 1
6 2


day_diff = 2

table[i][j] = max(table[i-1][j]+day[i]-day[i-1], table[i-1][j-1]+day_diff - gift[i])

0 3 5 6
0 3 5 6
1 1 3 
2
3
4

def get_gifts(days):
  table = [[0] * (len(days) + 1)] * (len(days) + 1)
  curr_money = days[0]
  for i, price in days:
    for j, price_j in range(len(days) + 1):
      table[day][day_j] = max(table[i-1][j]+day[i]-day[i-1], table[i-1][j-1]+day_diff - gift[i])

x = [[0]*3]*3
x[0][0] = 1
[[1, 0, 0], [1, 0, 0], [1, 0, 0]]









address book
___________________________________

address_book = [
    (number, street, city, country),
    ...
    (number, street, city, country),
]

address = (20, "Some street", "Warsaw", "PL")
address = (20, "Some street", None, "PL")   # we can use None as a wildcard

find_address(address)
# True - found
# False - not found


          country1
          /  |    \
     city1  city2  cityN
     /   \
street1  streetN
  / |  \
n1  n2  nN
















stackoverflow
___________________________________

# You run a support questions and answers website like StackOverflow. Recently, the amount of questions has grown dramatically.
# A group of engineers has volunteered to help but each volunteer has a prioritized list of tags they can support.
# Volunteers must be assigned questions with tags from their personal tags list. Here is example data in JSON form:

{
  "questions": [
    {
      "id": "0",
      "title": "how do i install vs code",
      "tags": ["mac", "vs code"]
    },
    {
      "id": "1",
      "title": "my program is too slow please help",
      "tags": ["python", "ai"]
    },
    {
      "id": "2",
      "title": "why is the hitbox off by 2 pixels",
      "tags": ["c#", "game"]
    },
    {
      "id": "3",
      "title": "my dependency injection stack trace is strange",
      "tags": ["java", "oop"]
    },
    {
      "id": "4",
      "title": "socket.recv is freezing",
      "tags": ["python", "networking"]
    },
    {
      "id": "5",
      "title": "i have a memory leak",
      "tags": ["c++", "networking"]
    }
  ],
  "volunteers": [
    {
      "id": "sam5k",
      "tags": ["python", "networking"]
    },
    {
      "id": "djpat",
      "tags": ["ai"]
    },
    {
      "id": "jessg",
      "tags": ["java", "networking"]
    },
    {
      "id": "rayo",
      "tags": ["java", "networking"]
    }
  ]
}

# Create a function that returns an assignments object like so:

[{'question': '1', 'volunteer': 'sam5k'},
 {'question': '3', 'volunteer': 'jessg'},
 {'question': '4', 'volunteer': 'rayo'}]

# Background
# - A solution that does not assign all volunteers is OK.
# - Each question must be assigned at most one volunteer.
# - Each volunteer must be assigned at most one question.
# - Volunteer tags must have an intersection of one or more tags with the question they are assigned.

{
  python: hashset[id1, id2, idN],  --> rm idN
  ai: hashset[id1, idN],   --- also rm IDN
}

{
      "id": "idN",
      "tags": ["python", "ai"]
}


def assign_questions(questions, volunteers):
  # create a map "tags - volunteers"
  tags_volunteers_map = collections.defaultdict(dict)
  for v in volunteers:
    if v.get("id") is None:
      continue
    if v.get("tags") is None:
      continue
      
    for tag in v["tags"]:
      tags_volunteers_map[tag][v["id"]] = None
      # {python: {sam5k: None}}
      # {python: {sam5k: None}
       # networking: {sam5k: None}}
  
  assigned_questions = []
  for q in questions:
    if q.get("id") is None:
      continue
    if q.get("tags") is None:
      continue
    
    # find a volunteer
    match_tag = None
    for q_tag in q["tags"]:
      if q_tag in tags_volunteers_map:
        match_tag = q_tag
        break
        
    if match_tag is None:
      # no matches for this question, skip it
      continue
      
    # assing a question
    assinged_volunteer_id = random.choice(tags_volunteers_map[match_tag])
    assigned_questions.append({
      "question": q["id"],
      "volunteer": assinged_volunteer_id,
    })
    # O(1), set of already assigned 
    # rm a volunteer from a waiting line
    for tag in tags_volunteers_map:
      del tags_volunteers_map[tag][assinged_volunteer_id]
  
  return assigned_questions