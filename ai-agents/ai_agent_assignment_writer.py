import random

def generate_assignment(topic):
    topic_cap = topic.strip().title()

    intro_templates = [
        f"\nAssignment on **{topic_cap}**\n\n{topic_cap} is an important concept that plays a major role in understanding modern scientific and social systems.",
        f"\nDetailed Assignment on **{topic_cap}**\n\nThe topic of {topic_cap} holds great relevance in today’s world.",
        f"\nExplanation of **{topic_cap}**\n\n{topic_cap} is a concept that helps us understand various aspects of life and the environment around us."
    ]

    body_templates = [
        f"\n1. **Introduction to {topic_cap}:**\n   {topic_cap} refers to a subject that has broad application across multiple fields. It provides essential background knowledge needed for higher understanding.",
        f"\n2. **Importance of {topic_cap}:**\n   This topic is important because it influences various biological, environmental, technological, or social processes.",
        f"\n3. **Key Features of {topic_cap}:**\n   Several fundamental ideas are associated with {topic_cap}. These features help define its role and application.",
        f"\n4. **Applications of {topic_cap}:**\n   {topic_cap} is applied in real life, academic research, industry, and education. It helps solve major problems and improves knowledge.",
        f"\n5. **Impact of {topic_cap}:**\n   The topic has a significant impact on science, society, and daily life. It helps shape human understanding and development."
    ]

    conclusion_templates = [
        f"\nConclusion:\nIn conclusion, {topic_cap} is a valuable topic that provides deep insight into many areas. Understanding this topic helps in academic growth and real-world applications.",
        f"\nConclusion:\nTo summarise, {topic_cap} remains a crucial concept that continues to influence scientific and social progress.",
        f"\nConclusion:\nOverall, {topic_cap} is an essential topic that broadens knowledge and opens new learning opportunities."
    ]

    assignment = (
        random.choice(intro_templates)
        + "\n"
        + "".join(random.sample(body_templates, 3))
        + "\n"
        + random.choice(conclusion_templates)
    )

    return assignment


def assignment_agent():
    print("📝 Universal Assignment Writer Agent Ready!")
    print("Type any topic (example: 'Global Warming', 'Cell Division').")
    print("Type 'exit' to stop.\n")

    while True:
        topic = input("Enter topic: ").strip().lower()

        if topic == "exit":
            print("Goodbye! Your assignments are ready 😄")
            break

        print("\n" + generate_assignment(topic))
        print("\n" + "-"*60 + "\n")


assignment_agent()
