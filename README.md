# Automotive FAQ Assistant

A source-grounded Automotive FAQ Assistant inspired by GenAI principles.  
The system answers vehicle-related questions by retrieving relevant sections from a car manual and generating reliable, explainable responses.

---

## Project Overview

Car manuals contain essential information but are often difficult to search quickly.
This project addresses that problem by allowing users to ask natural-language questions about a vehicle and receive accurate answers grounded strictly in the vehicle manual.

The focus of this project is not on training AI models, but on designing a responsible GenAI-style system that emphasizes retrieval, transparency, and reliability.

---

## How It Works

1. The vehicle manual is stored as structured text data.
2. The user asks a natural language question about the vehicle.
3. The system matches the question against predefined manual sections.
4. The most relevant section is retrieved.
5. An answer is generated strictly from that section.
6. The response is displayed along with the source section name.

This workflow follows a retrieval-based, source-grounded approach inspired by Generative AI systems.

---

## Source-Aware Answering

To prevent AI hallucinations and incorrect responses, the assistant only answers questions if the information is present in the vehicle manual.
If the required information is not found, the system clearly states that the information is unavailable.

Each response includes a reference to the manual section used, improving transparency and user trust.

---

## Project Structure

automotive-faq-assistant/
│
├── app.py
├── README.md
├── data/
│ └── car_manual.txt
├── docs/
│ └── project_documentation.md
└── linkedin_post.md

---

## Technologies Used

- Python
- Structured text data
- Retrieval-based logic
- Source-grounded response design

---

## Limitations

- The current version supports a single vehicle manual.
- Section retrieval is keyword-based.
- The system runs locally and does not use external AI APIs.

These limitations are intentional to keep the project simple, explainable, and suitable for learning.

---

## Future Enhancements

- Support for multiple vehicle manuals.
- Advanced retrieval using embeddings and vector search.
- Integration with real GenAI APIs.
- Web-based interface for improved usability.

---

## Conclusion

This project demonstrates how GenAI concepts can be applied responsibly in a safety-critical domain like automotive assistance.
By focusing on retrieval, source awareness, and explainability, the system prioritizes trust and correctness over uncontrolled text generation.
