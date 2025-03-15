import pandas as pd
import os

def main():
    # Load the CSV file
    file_path = os.path.join('data', 'Effects of Violent Video Games on Aggression CSV MSDOS.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(df.head())
        print(df.columns)
    else:
        print(f"File not found: {file_path}")
        return
    # Define the aggression questions
    agression_questions = [
        "Some of my Friends think I am hothead",
        "If I have to resort to violence to protect my rights, I will",
        "When people are especially nice to me, I wonder what they want",
        "I tell my friends openly when I disagree with them",
        "Once I became so mad, I broke things",
        "When people disagree with me I get into arguments",
        "When I argue I use abusive language",
        "I am a hot-tempered person",
        "I am suspicious of strangers who are too friendly",
        "I have threatened some people whom I know",
        "I can get angry suddenly but get over it quickly",
        "If I am provoked enough, I will hit another person",
        "When people annoy me, I openly tell them what I think of them",
        "I may hit a person for no good reason",
        "Sometimes I feel I am being treated unfairly",
        "I have trouble controlling my temper",
        "When frustrated, I show my irritation",
        "Sometimes I feel people are laughing behind my back",
        "I often disagree with people",
        "If somebody hits me, I hit back",
        "I sometimes feel like exploding for no good reason",
        "I feel other people always take over the oppurtunity and I miss it",
        "there are people who pushed me so far that we begin fighting",
        'I know that some so called "friends" talk about me behind my back',
        "My friends say that I am a bit argumentative",
        "Sometimes I lose temper for no good reason",
        "I get into fights a little more than a normal person",
        "sometimes I can not control the feeling to hit another person ",
        "I sometimes get too much jealous from people",
        "I dont know why sometimes I feel bitter about things"
    ]
    # Map the responses to scores
    response_map = {
        "strongly Agree": 5,
        "Agree": 4,
        "Neither Agree Nor Disagree": 3,
        "Disagree": 2,
        "strongly Disagree": 1
    }
    # Calculate the aggression score for each user
    results = []
    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Create a unique user ID
        user_id = f"User {index + 1}"
        # Calculate the aggression score
        scores = [response_map.get(row[question], None) for question in agression_questions]
        # Filter out None values
        valid_scores = [score for score in scores if score is not None]
        # Calculate the average aggression score
        aggesion_score = sum(valid_scores) / len(valid_scores) if valid_scores else None
        # Append the result to the list
        results.append({
            "User ID": user_id,
            "Aggression Score": aggesion_score
        })
    # Create a DataFrame from the results
    results_df = pd.DataFrame(results)
    print(results_df)

    # Save the results to a text file and an Excel file
    with open("results.txt", "w") as f:
        for index, row in results_df.iterrows():
            f.write(f"{row['User ID']}: {row['Aggression Score']}\n")
    
    results_df.to_excel("results.xlsx", index=False, engine='openpyxl')

if __name__ == "__main__":
    main()