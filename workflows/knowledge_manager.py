from prompts.knowledge_prompts import knowledge_prompt

def generate_knowledge(topic):
    prompt = knowledge_prompt(topic)

    # Simulated AI response (for academic/demo use)
    return f"""
ORGANIZATIONAL KNOWLEDGE DOCUMENT

Topic: {topic}

Overview:
This document explains {topic} in a clear and structured manner for organizational use.

Key Information:
- Definition and purpose of {topic}
- Roles and responsibilities
- Guidelines and procedures

Best Practices:
- Follow standardized processes
- Ensure regular updates
- Maintain clear documentation

Organizational Use:
This knowledge helps employees understand policies, improves efficiency,
and ensures consistency across departments.

Summary:
Effective knowledge management of {topic} supports better decision-making
and organizational growth.
"""