def flames_game(name1, name2):
    # Preprocess names
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    # Create a combined list of characters from both names
    combined_chars = list(name1 + name2)
    
    # Remove common characters
    for char in set(name1) & set(name2):
        count = min(name1.count(char), name2.count(char))
        for _ in range(count):
            combined_chars.remove(char)
            combined_chars.remove(char)
    
    # Calculate the number of unique characters left
    count = len(combined_chars)
    
    # FLAMES logic
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    
    while len(flames) > 1:
        # Find the index to remove
        index = (count - 1) % len(flames)
        flames.pop(index)
        
    return flames[0]

def main():
    print("Welcome to the FLAMES game!")
    # name1 = input("Enter the first name: ")
    # name2 = input("Enter the second name: ")
    name1 = 'sathish'
    name2 = 'priyanka'
    
    relationship = flames_game(name1, name2)
    
    relationship_dict = {
        'F': "Friends",
        'L': "Love",
        'A': "Affection",
        'M': "Marriage",
        'E': "Enemy",
        'S': "Sister"
    }
    
    print(f"The relationship between {name1} and {name2} is: {relationship_dict[relationship]}")

if __name__ == "__main__":
    main()