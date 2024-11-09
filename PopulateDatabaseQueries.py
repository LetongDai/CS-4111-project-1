# in case we mess up stuff in the database, just use this
import random
usernames = [
    "TechSavvy23",
    "QuantumRider",
    "PixelPioneer",
    "NeonWanderer",
    "CodeCrafterX",
    "GalacticNomad",
    "CyberPhoenix",
    "AuroraChaser",
    "MidnightCoder",
    "EchoBlaze",
    "LunarVoyager",
    "FrostByteZ",
    "StarryNavigator",
    "NovaSeeker42",
    "ElectroSurge"
] # All from ChatGPT

user_query = "INSERT INTO users (uid, username) VALUES "

for i,username in enumerate(usernames):
    user_query += f"({i + 1}, \'{username}\'), "
user_query = user_query[:-2] + ';'

print(user_query)

topics = [
    "Physics",
    "Biology",
    "Mathematics",
    "Chemistry",
    "History",
    "Literature",
    "Philosophy",
    "Economics",
    "Psychology",
    "Sociology",
    "Political Science",
    "Art History",
    "Geography",
    "Statistics",
    "Zoology"
]

topic_query = "INSERT INTO topics (tid, topic) VALUES "

for i,topic in enumerate(topics):
    topic_query += f"({i + 1}, \'{topic}\'), "
topic_query = topic_query[:-2] + ';'

print(topic_query)

user_map = {username: i + 1 for i, username in enumerate(usernames)}
print(user_map)
topic_map = {topic: i + 1 for i, topic in enumerate(topics)}
print(topic_map)

questions = {
    "What are the fundamental laws of physics?": topic_map["Physics"],
    "What are the main theories of evolution in biology?": topic_map["Biology"],
    "How do you apply calculus in real-life scenarios?": topic_map["Mathematics"],
    "What are the most important chemical reactions to know?": topic_map["Chemistry"],
    "How has history shaped modern society?": topic_map["History"],
    "What themes are most prevalent in 21st-century literature?": topic_map["Literature"],
    "What is the significance of ethics in philosophy?": topic_map["Philosophy"],
    "How does economic policy affect global markets?": topic_map["Economics"],
    "What are the psychological impacts of social media?": topic_map["Psychology"],
    "How do sociological factors influence behavior?": topic_map["Sociology"],
    "What are the major political ideologies in the world?": topic_map["Political Science"],
    "How has art influenced culture throughout history?": topic_map["Art History"],
    "What role does geography play in shaping societies?": topic_map["Geography"],
    "How is statistics used to analyze data?": topic_map["Statistics"],
    "What is the coolest animal?": topic_map["Zoology"]
}

question_map = {question: i + 1 for i,question in enumerate(questions)}

question_query = "INSERT INTO questions (qid, text, date, uid) VALUES "
random_uids = [2, 7, 11, 6, 3, 14, 4, 8, 15, 12, 9, 1, 10, 13, 5]
for i,question in enumerate(questions):
    question_query += f"({i + 1}, \'{question}\', NOW(), {random_uids[i]}), "
question_query = question_query[:-2] + ';'

print(question_query)

belongtorelation_query = "INSERT INTO belongtorelations (qid, tid) VALUES "
for i,_ in enumerate(questions):
    belongtorelation_query += f"({i + 1}, {i+1}), "
belongtorelation_query = belongtorelation_query[:-2] + ';'

print(belongtorelation_query)

answers = {
    "What are the fundamental laws of physics?":
        "Newtons Laws of Motion (Inertia, F=ma, Action-Reaction), Law of Universal Gravitation, Conservation Laws (Energy, Momentum, Charge), Laws of Thermodynamics (Zeroth, First, Second, Third)",

    "What are the main theories of evolution in biology?":
        "Natural Selection, Genetic Drift, Mutation, Gene Flow, and the Modern Synthesis, which combines Darwinian evolution with Mendelian genetics.",

    "How do you apply calculus in real-life scenarios?":
        "Calculus is used in fields such as physics for motion analysis, economics for cost and revenue optimization, biology for population modeling, and engineering for designing structures.",

    "What are the most important chemical reactions to know?":
        "Combustion, Acid-Base Neutralization, Precipitation Reactions, Redox Reactions, and Hydrolysis.",

    "How has history shaped modern society?":
        "Historical events, such as wars, revolutions, and social movements, have influenced political systems, cultural norms, technological advancements, and economic structures.",

    "What themes are most prevalent in 21st-century literature?":
        "Identity, globalization, technology, social justice, climate change, and the impact of digital culture.",

    "What is the significance of ethics in philosophy?":
        "Ethics explores moral principles, guiding human behavior and decision-making, influencing laws, social norms, and personal values.",

    "How does economic policy affect global markets?":
        "Economic policies influence trade, investment, inflation rates, and currency values, impacting international relations and economic stability.",

    "What are the psychological impacts of social media?":
        "Social media can lead to increased connectivity but may also cause anxiety, depression, cyberbullying, and distorted self-image.",

    "How do sociological factors influence behavior?":
        "Sociological factors such as culture, social class, family dynamics, and peer pressure significantly shape individual and group behavior.",

    "What are the major political ideologies in the world?":
        "Liberalism, Conservatism, Socialism, Communism, Fascism, and Anarchism are among the most prominent political ideologies.",

    "How has art influenced culture throughout history?":
        "Art reflects societal values, challenges norms, inspires movements, and fosters dialogue about identity, power, and change.",

    "What role does geography play in shaping societies?":
        "Geography influences resource distribution, climate, culture, trade routes, and social interactions, shaping economic and political systems.",

    "How is statistics used to analyze data?":
        "Statistics provides tools for collecting, analyzing, interpreting, and presenting data, essential for decision-making in various fields.",

    "What is the coolest animal?":
        "The octopus is often considered one of the coolest animals due to its intelligence, ability to change color, and unique behaviors."
}

answer_query = "INSERT INTO answers (qid, aid, text, date, uid) VALUES "
random_uids_TWO = [11, 8, 15, 9, 3, 12, 2, 7, 1, 10, 13, 6, 5, 4, 14]
for i,question in enumerate(answers):
    answer_query += f"({question_map[question]}, {i + 1}, \'{answers[question]}\', NOW(), {random_uids_TWO[i]}), "
answer_query = answer_query[:-2] + ';'

print(answer_query)

announcements= {
    "Physics":
        "Join us for an exciting exploration of Physics! Discover the fundamental laws that govern the universe and the groundbreaking discoveries shaping our understanding of reality.",

    "Biology":
        "Dive into the fascinating world of Biology! Explore the intricacies of life, from cellular processes to ecosystems, and learn about the theories that explain the diversity of living organisms.",

    "Mathematics":
        "Get ready for an engaging discussion on Mathematics! From algebra to calculus, we will uncover the beauty and applications of mathematical concepts in everyday life.",

    "Chemistry":
        "Join us for a thrilling session on Chemistry! Discover the essential chemical reactions that form the basis of our material world and the role of chemistry in various industries.",

    "History":
        "Explore the rich tapestry of History with us! Learn how past events and movements have shaped our modern society and continue to influence our world today.",

    "Literature":
        "Join our discussion on Literature! We’ll delve into the themes, styles, and significant works that define 21st-century literature and reflect societal values.",

    "Philosophy":
        "Engage in a thought-provoking conversation about Philosophy! Discover the significance of ethical frameworks and how they influence our understanding of morality and society.",

    "Economics":
        "Don’t miss our upcoming seminar on Economics! Explore how economic policies shape global markets and influence everyday life in our interconnected world.",

    "Psychology":
        "Join us for an insightful discussion on Psychology! We will examine the psychological impacts of social media and other factors that influence human behavior.",

    "Sociology":
        "Explore the fascinating field of Sociology! Learn about the sociological factors that influence behavior and how they shape social dynamics in various communities.",

    "Political Science":
        "Dive into the world of Political Science! Join us as we discuss major political ideologies and their impact on global politics and governance.",

    "Art History":
        "Join us for an exploration of Art History! Discover how art movements have influenced culture and society throughout history and continue to resonate today.",

    "Geography":
        "Explore the vital role of Geography in shaping societies! We will discuss how geographic factors influence culture, economy, and political systems around the world.",

    "Statistics":
        "Don’t miss our session on Statistics! Learn how statistical methods are used to analyze data, make informed decisions, and understand trends in various fields.",

    "Zoology":
        "Join us for an exciting journey into Zoology! Discover the diversity of animal life, their behaviors, and the ecological roles they play in our ecosystems."
}



announcement_query = "INSERT INTO announcements (announce_id, text, tid, date) VALUES "
for i,announce in enumerate(announcements):
    announcement_query += f"({i + 1}, \'{announcements[announce]}\', {topic_map[announce]}, NOW()), "
announcement_query = announcement_query[:-2] + ';'

print(announcement_query)