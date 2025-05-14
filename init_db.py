import sqlite3

def initialize_database():
    conn = sqlite3.connect('bible_game.db')
    cursor = conn.cursor()

    # Create questions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            reference TEXT NOT NULL
        )
    ''')

    # Insert sample data
    cursor.executemany('''
        INSERT INTO questions (question, option1, option2, option3, correct_answer, reference)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', [
        ("What is the first book of the Bible?", "Genesis", "Exodus", "Leviticus", "Genesis", "Genesis 1:1"),
        ("Who built the ark?", "Moses", "Noah", "Abraham", "Noah", "Genesis 6:14"),
        ("What is the shortest verse in the Bible?", "Jesus wept.", "God is love.", "Pray without ceasing.", "Jesus wept.", "John 11:35"),
        ("Who was swallowed by a great fish?", "Jonah", "Elijah", "Daniel", "Jonah", "Jonah 1:17"),
        ("What is the last book of the Bible?", "Revelation", "Jude", "Acts", "Revelation", "Revelation 22:21"),
        ("Who led the Israelites out of Egypt?", "Moses", "Joshua", "Aaron", "Moses", "Exodus 3:10"),
        ("What is the first commandment?", "You shall have no other gods before me.", "Honor your father and mother.", "You shall not steal.", "You shall have no other gods before me.", "Exodus 20:3"),
        ("Who was the strongest man in the Bible?", "Samson", "David", "Goliath", "Samson", "Judges 16:17"),
        ("Who was the wisest man in the Bible?", "Solomon", "David", "Samuel", "Solomon", "1 Kings 4:30"),
        ("What is the longest book in the Bible?", "Psalms", "Isaiah", "Genesis", "Psalms", "Psalms 119"),
        ("Who was the first king of Israel?", "Saul", "David", "Solomon", "Saul", "1 Samuel 10:1"),
        ("What is the greatest commandment?", "Love the Lord your God with all your heart.", "Do not murder.", "Do not commit adultery.", "Love the Lord your God with all your heart.", "Matthew 22:37")
    ])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()
    print("Database initialized with sample data.")