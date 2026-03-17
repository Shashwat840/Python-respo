#find heighest wicket taker and heighest run scorer
india_match = {
    "Sanju Samson": {
        "role": "Batsman",
        "runs_scored": 88,
        "wickets_taken": 0
    },
    "Abhishek Sharma": {
        "role": "All-rounder",
        "runs_scored": 51,
        "wickets_taken": 0
    },
    "Ishan Kishan": {
        "role": "Batsman",
        "runs_scored": 50,
        "wickets_taken": 0
    },
    "Shivam Dube": {
        "role": "All-rounder",
        "runs_scored": 30,
        "wickets_taken": 0
    },
    "Hardik Pandya": {
        "role": "All-rounder",
        "runs_scored": 12,
        "wickets_taken": 1
    },
    "Jasprit Bumrah": {
        "role": "Bowler",
        "runs_scored": 0,
        "wickets_taken": 4
    },
    "Varun Chakravarthy": {
        "role": "Bowler",
        "runs_scored": 0,
        "wickets_taken": 2
    },
    "Arshdeep Singh": {
        "role": "Bowler",
        "runs_scored": 0,
        "wickets_taken": 1
    }
}
max_runs = 0
max_wickets = 0
highestWicketTaker = "" 
highestRunScorer = ""
for player , score in india_match.items():
    if score["runs_scored"] > max_runs:
        max_runs = score["runs_scored"]
        highestRunScorer = player
    if score["wickets_taken"] > max_wickets:
        max_wickets = score["wickets_taken"]
        highestWicketTaker = player
print(f"Highest Run: {highestRunScorer} , runs {max_runs} ")
print(f"Highest Wicket: {highestWicketTaker} , Wickets {max_wickets} ")
