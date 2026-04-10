from app import app
from models import db, Topic, Media, TopicReference


TOPICS_DATA = [
    {
        "id": 1,
        "slug": "turing-thoughts-on-ai",
        "title": "Alan Turing's Thoughts on AI",
        "yearRange": "c. 1950",
        "category": "Foundations",
        "status": "Legacy",
        "introText": "Alan Turing's ideas laid the intellectual groundwork for artificial intelligence. His questions about whether machines can think became central to later AI research.",
        "shortSummary": "Turing provided the conceptual foundations for machine intelligence.",
        "howItWorks": "This topic focuses on theoretical ideas about computation, intelligence, and symbolic reasoning rather than a single application system.",
        "simpleExample": "A machine following formal logical steps to solve a problem reflects Turing's vision of computation.",
        "effectiveUse": "Most effective in foundational teaching, philosophy of AI, and computational theory.",
        "realWorldExamples": "University teaching, theoretical computer science, and early AI research.",
        "advantages": "Provides a strong conceptual basis for later technologies.",
        "limitations": "Highly theoretical and not a direct end-user system.",
        "misuse": "Can be oversimplified when discussing modern AI.",
        "ethics": "Raises questions about intelligence, autonomy, and human-machine comparison.",
        "waContext": "The University of Western Australia's Computer Science department has long incorporated Turing's theories into its foundational curriculum.",
        "media": [
            {
                "id": 1,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1200&q=80",
                "title": "Computing Foundations",
                "caption": "Theoretical work shaped the future of AI."
            }
        ],
        "references": [
            {
                "id": 1,
                "title": "Foundational AI History",
                "url": "https://en.wikipedia.org/wiki/Alan_Turing",
                "sourceType": "Background Source",
                "accessedDate": "Accessed 2026",
                "notes": "General background on Turing and computing history."
            }
        ]
    },
    {
        "id": 2,
        "slug": "learning-machines",
        "title": "Learning Machines",
        "yearRange": "c. 1960",
        "category": "Machine Learning",
        "status": "Active",
        "introText": "Learning machines marked a shift from explicit programming toward systems that could improve through data and experience.",
        "shortSummary": "Machines began to learn patterns rather than rely only on fixed hand-written rules.",
        "howItWorks": "These systems use training data to identify patterns and improve decision-making over time.",
        "simpleExample": "A model trained on past weather data predicts tomorrow's temperature range.",
        "effectiveUse": "Useful when large amounts of data are available and patterns can be learned statistically.",
        "realWorldExamples": "Prediction systems, classification, industrial monitoring, and analytics.",
        "advantages": "Can adapt better than rigid rule-based systems in changing environments.",
        "limitations": "Needs data quality, computational power, and careful evaluation.",
        "misuse": "Can produce misleading results when trained on biased or poor-quality data.",
        "ethics": "Raises concerns about fairness, transparency, and accountability.",
        "waContext": "WA universities and research groups have contributed to machine learning education and research.",
        "media": [
            {
                "id": 2,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=1200&q=80",
                "title": "Learning from Data",
                "caption": "Data-driven approaches transformed AI development."
            }
        ],
        "references": [
            {
                "id": 2,
                "title": "Machine Learning Overview",
                "url": "https://en.wikipedia.org/wiki/Machine_learning",
                "sourceType": "Background Source",
                "accessedDate": "Accessed 2026",
                "notes": "General introductory material."
            }
        ]
    },
    {
        "id": 3,
        "slug": "game-playing-ai",
        "title": "Game Playing AI",
        "yearRange": "c. 1970",
        "category": "Strategic Systems",
        "status": "Active",
        "introText": "Game-playing AI demonstrated that machines could make strategic decisions in structured environments.",
        "shortSummary": "Game AI made abstract reasoning and search visible and measurable.",
        "howItWorks": "These systems explore possible future moves and evaluate game states to choose effective strategies.",
        "simpleExample": "A chess engine examines several possible moves and chooses the one with the highest evaluation.",
        "effectiveUse": "Best in structured problems with clear rules and goals.",
        "realWorldExamples": "Chess engines, board games, and teaching search algorithms.",
        "advantages": "Excellent for demonstrating planning and search methods.",
        "limitations": "Performs best in closed systems with well-defined rules.",
        "misuse": "People may assume success in games always transfers to messy real-world tasks.",
        "ethics": "Limited direct ethical risk, but influences public perception of AI capability.",
        "waContext": "WA computing programs have used game-playing systems as teaching tools for search, heuristics, and decision-making.",
        "media": [
            {
                "id": 3,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1528819622765-d6bcf132f793?auto=format&fit=crop&w=1200&q=80",
                "title": "Strategic Search",
                "caption": "Game environments provided clear testbeds for AI reasoning."
            }
        ],
        "references": [
            {
                "id": 3,
                "title": "Game AI Background",
                "url": "https://en.wikipedia.org/wiki/Game_artificial_intelligence",
                "sourceType": "Background Source",
                "accessedDate": "Accessed 2026",
                "notes": "General overview source."
            }
        ]
    },
    {
        "id": 4,
        "slug": "expert-systems",
        "title": "Expert Systems",
        "yearRange": "c. 1980",
        "category": "Knowledge Engineering",
        "status": "Legacy",
        "introText": "In the 1980s, expert systems became the first commercially successful form of AI. These programs encoded the decision-making knowledge of human experts into software using rules, facts, and inference engines.",
        "shortSummary": "Expert systems captured human specialist knowledge in rule-based software, enabling computers to make decisions in medicine, finance, and engineering by following chains of if-then logic.",
        "howItWorks": "An expert system consists of a knowledge base, an inference engine, and a user interface. The inference engine applies rules step by step to reach a conclusion.",
        "simpleExample": "If a patient has fever and cough, and recently travelled, the system may suggest considering a tropical disease.",
        "effectiveUse": "Most effective in narrow domains where knowledge can be clearly expressed as rules.",
        "realWorldExamples": "MYCIN, DENDRAL, and XCON.",
        "advantages": "They preserve expert knowledge, provide consistent decisions, and work well in specialised areas.",
        "limitations": "They are brittle, hard to maintain, and struggle with uncertainty and ambiguity.",
        "misuse": "They can be misused when applied outside their narrow domain.",
        "ethics": "Important concerns include accountability, transparency, and over-reliance in high-stakes domains.",
        "waContext": "Expert systems influenced decision support work in WA across mining, agriculture, and environmental management.",
        "media": [
            {
                "id": 4,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=1200&q=80",
                "title": "Knowledge Engineering Process",
                "caption": "The process of capturing expert knowledge into rule-based systems."
            },
            {
                "id": 5,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=1200&q=80",
                "title": "Medical Expert Systems",
                "caption": "Expert systems found early success in medical diagnosis."
            }
        ],
        "references": [
            {
                "id": 4,
                "title": "Rule-based Expert Systems",
                "url": "https://en.wikipedia.org/wiki/Expert_system",
                "sourceType": "Background Source",
                "accessedDate": "Accessed 2026",
                "notes": "General overview of expert systems."
            }
        ]
    },
    {
        "id": 5,
        "slug": "artificial-neural-nets",
        "title": "Artificial Neural Networks",
        "yearRange": "1980–2000",
        "category": "Neural Computing",
        "status": "Active",
        "introText": "Artificial neural networks experienced a renaissance in the 1980s with the development of backpropagation.",
        "shortSummary": "Inspired by the human brain, artificial neural networks learned complex patterns through layers of interconnected nodes.",
        "howItWorks": "A neural network consists of layers of artificial neurons. Data enters the input layer, passes through hidden layers, and produces output.",
        "simpleExample": "Imagine a team passing a message through a chain, then adjusting after feedback until the message becomes reliable.",
        "effectiveUse": "Pattern recognition in images, speech, and text.",
        "realWorldExamples": "Handwriting recognition, speech recognition, financial prediction, and medical image analysis.",
        "advantages": "Learns complex non-linear patterns and generalises to new data.",
        "limitations": "Needs large amounts of data and is often difficult to explain.",
        "misuse": "Biased training data can lead to biased outcomes in decision systems.",
        "ethics": "Raises accountability concerns because decisions are often hard to explain.",
        "waContext": "WA universities, particularly UWA and Curtin, established neural computing research groups in the 1990s.",
        "media": [
            {
                "id": 6,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600",
                "title": "Neural Network Architecture",
                "caption": "Visualisation of neural network layers and connections"
            },
            {
                "id": 7,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1559757175-5700dde675bc?w=600",
                "title": "Brain-Inspired Computing",
                "caption": "Neural networks drew inspiration from biological neural structures"
            }
        ],
        "references": [
            {
                "id": 5,
                "title": "Learning Representations by Back-propagating Errors",
                "url": "https://www.nature.com/articles/323533a0",
                "sourceType": "Research Paper",
                "accessedDate": "2024-02-15",
                "notes": "Rumelhart, Hinton & Williams' seminal 1986 paper"
            },
            {
                "id": 6,
                "title": "Neural Networks and Deep Learning",
                "url": "http://neuralnetworksanddeeplearning.com/",
                "sourceType": "Online Book",
                "accessedDate": "2024-02-15",
                "notes": "Michael Nielsen's accessible introduction"
            }
        ]
    },
    {
        "id": 6,
        "slug": "internet-driven-ai-ibm-watson",
        "title": "Internet-Driven AI / IBM Watson",
        "yearRange": "c. 2011",
        "category": "Knowledge Retrieval",
        "status": "Legacy",
        "introText": "IBM Watson showed that AI could process enormous volumes of unstructured text, understand natural language questions, and answer in real time.",
        "shortSummary": "IBM Watson demonstrated large-scale knowledge-driven AI.",
        "howItWorks": "Watson used a massively parallel architecture called DeepQA to generate, score, and rank candidate answers.",
        "simpleExample": "Imagine a thousand researchers searching millions of documents at once, each proposing an answer with a confidence score.",
        "effectiveUse": "Question answering, information retrieval, medical literature analysis, legal review.",
        "realWorldExamples": "Jeopardy!, Watson for Oncology, enterprise assistants.",
        "advantages": "Processes and synthesises information from huge document collections.",
        "limitations": "Requires major computing resources and struggled in messy real-world domains.",
        "misuse": "Overhyped marketing can lead organisations to trust the system beyond its real capabilities.",
        "ethics": "Raises accountability concerns in healthcare and other high-stakes domains.",
        "waContext": "WA healthcare and resources sectors explored Watson-style AI for analysis and decision support.",
        "media": [
            {
                "id": 8,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=600",
                "title": "Watson on Jeopardy!",
                "caption": "AI competing against human champions in knowledge retrieval"
            },
            {
                "id": 9,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600",
                "title": "Big Data Processing",
                "caption": "The massive data processing infrastructure behind Watson"
            }
        ],
        "references": [
            {
                "id": 7,
                "title": "Building Watson: An Overview of the DeepQA Project",
                "url": "https://www.aaai.org/ojs/index.php/aimagazine/article/view/2303",
                "sourceType": "Research Paper",
                "accessedDate": "2024-02-20",
                "notes": "IBM Research's technical overview of Watson's architecture"
            },
            {
                "id": 8,
                "title": "Watson: Beyond Jeopardy!",
                "url": "https://www.ibm.com/watson",
                "sourceType": "Web Archive",
                "accessedDate": "2024-02-20",
                "notes": "IBM's Watson platform documentation"
            }
        ]
    },
    {
        "id": 7,
        "slug": "evolutionary-computing-genetic-algorithms",
        "title": "Evolutionary Computing & Genetic Algorithms",
        "yearRange": "c. 2010",
        "category": "Bio-Inspired AI",
        "status": "Active",
        "introText": "Evolutionary computing draws inspiration from biological evolution to optimise complex problems.",
        "shortSummary": "Genetic algorithms apply natural selection to computing.",
        "howItWorks": "A genetic algorithm starts with random candidate solutions, evaluates them, selects the best, and creates new generations via crossover and mutation.",
        "simpleExample": "Like designing better paper airplanes by repeatedly keeping the best and combining their features.",
        "effectiveUse": "Optimisation problems in engineering, logistics, scheduling, and design.",
        "realWorldExamples": "NASA antenna design, logistics routing, financial strategy evolution.",
        "advantages": "Works well on complex search spaces and can find creative solutions.",
        "limitations": "Computationally expensive and does not guarantee the global optimum.",
        "misuse": "Can be used to optimise harmful or adversarial outcomes if the fitness criteria are poorly designed.",
        "ethics": "Optimization goals must be defined carefully to avoid harmful unintended consequences.",
        "waContext": "WA researchers have used genetic algorithms in mining optimisation and logistics.",
        "media": [
            {
                "id": 10,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1530026405186-ed1f139313f8?w=600",
                "title": "Evolutionary Process Diagram",
                "caption": "The cycle of selection, crossover, and mutation in genetic algorithms"
            },
            {
                "id": 11,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1500462918059-b1a0cb512f1d?w=600",
                "title": "Optimisation in Nature",
                "caption": "Nature's evolutionary processes inspire computational optimisation"
            }
        ],
        "references": [
            {
                "id": 9,
                "title": "Genetic Algorithms in Search, Optimization and Machine Learning",
                "url": "https://dl.acm.org/doi/book/10.5555/534133",
                "sourceType": "Book",
                "accessedDate": "2024-03-01",
                "notes": "Goldberg's foundational textbook on genetic algorithms"
            },
            {
                "id": 10,
                "title": "Evolutionary Computation: Toward a New Philosophy of Machine Intelligence",
                "url": "https://ieeexplore.ieee.org/",
                "sourceType": "Book",
                "accessedDate": "2024-03-01",
                "notes": "Fogel's comprehensive overview of the field"
            }
        ]
    },
    {
        "id": 8,
        "slug": "synthetic-media-technology-deep-fakes",
        "title": "Synthetic Media Technology / Deep Fakes",
        "yearRange": "c. 2015",
        "category": "Generative AI & Deception",
        "status": "Active",
        "introText": "Deep fakes use neural networks to create highly realistic fake media.",
        "shortSummary": "Deep fake technology creates convincing fake images, audio, and video.",
        "howItWorks": "Most deep fakes use GANs, where a generator and discriminator compete to improve realism and detection.",
        "simpleExample": "Like two art students: one creates forgeries, the other tries to detect them, both improving over time.",
        "effectiveUse": "Film, accessibility, art, privacy protection, and synthetic data generation.",
        "realWorldExamples": "Face-swapping in films, voice cloning, manipulated political or intimate media.",
        "advantages": "Powerful creative applications and privacy-preserving possibilities.",
        "limitations": "Detection remains difficult and fakes often spread faster than debunking.",
        "misuse": "Non-consensual imagery, political disinformation, voice fraud, fabricated evidence.",
        "ethics": "Raises urgent concerns around consent, evidence, trust, and democracy.",
        "waContext": "WA law enforcement and cybersecurity researchers have studied deep fake detection and digital forensics.",
        "media": [
            {
                "id": 12,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600",
                "title": "Synthetic Media Generation",
                "caption": "The technology behind generating synthetic media content"
            },
            {
                "id": 13,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1563986768609-322da13575f2?w=600",
                "title": "Digital Forensics",
                "caption": "Digital forensics tools used to detect manipulated media"
            }
        ],
        "references": [
            {
                "id": 11,
                "title": "Generative Adversarial Networks",
                "url": "https://arxiv.org/abs/1406.2661",
                "sourceType": "Research Paper",
                "accessedDate": "2024-03-10",
                "notes": "Goodfellow et al.'s original GAN paper"
            },
            {
                "id": 12,
                "title": "The State of Deepfakes",
                "url": "https://regmedia.co.uk/2019/10/08/deepfake_report.pdf",
                "sourceType": "Report",
                "accessedDate": "2024-03-10",
                "notes": "Deeptrace's analysis of deep fake proliferation"
            }
        ]
    },
    {
        "id": 9,
        "slug": "natural-language-processing",
        "title": "Natural Language Processing",
        "yearRange": "2010–2020",
        "category": "Language AI",
        "status": "Active",
        "introText": "Natural Language Processing (NLP) transformed how computers understand and generate human language.",
        "shortSummary": "NLP enabled machine translation, sentiment analysis, and the precursors to modern AI assistants.",
        "howItWorks": "Modern NLP uses embeddings and Transformer architectures to represent and process language contextually.",
        "simpleExample": "A Transformer connects words in a sentence to understand which ones refer to each other.",
        "effectiveUse": "Machine translation, summarisation, question answering, sentiment analysis, chatbots.",
        "realWorldExamples": "Google Translate, virtual assistants, Gmail Smart Reply, sentiment analysis tools.",
        "advantages": "Allows computers to work with language at useful quality and scale.",
        "limitations": "Can struggle with sarcasm, irony, and cultural nuance.",
        "misuse": "Spam, disinformation, surveillance, manipulative targeting.",
        "ethics": "Bias in language data can produce unfair or exclusionary outcomes at scale.",
        "waContext": "WA researchers have applied NLP in mining documents, environmental assessments, and language projects.",
        "media": [
            {
                "id": 14,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600",
                "title": "Language Processing Pipeline",
                "caption": "The complex pipeline of processing natural language"
            },
            {
                "id": 15,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600",
                "title": "Transformer Architecture",
                "caption": "The Transformer architecture revolutionised NLP"
            }
        ],
        "references": [
            {
                "id": 13,
                "title": "Attention Is All You Need",
                "url": "https://arxiv.org/abs/1706.03762",
                "sourceType": "Research Paper",
                "accessedDate": "2024-03-15",
                "notes": "The foundational Transformer paper by Vaswani et al."
            },
            {
                "id": 14,
                "title": "Efficient Estimation of Word Representations in Vector Space",
                "url": "https://arxiv.org/abs/1301.3781",
                "sourceType": "Research Paper",
                "accessedDate": "2024-03-15",
                "notes": "Mikolov et al.'s Word2Vec paper"
            }
        ]
    },
    {
        "id": 10,
        "slug": "large-language-models",
        "title": "Large Language Models",
        "yearRange": "2024",
        "category": "Frontier AI",
        "status": "Active",
        "introText": "Large Language Models (LLMs) scale Transformer architectures to enormous sizes and datasets.",
        "shortSummary": "LLMs like GPT-4, Claude, and Gemini represent the current frontier of AI.",
        "howItWorks": "LLMs are Transformer neural networks trained on vast corpora to predict next words and generate helpful outputs.",
        "simpleExample": "Like someone who has read almost everything and answers by predicting the most useful response word by word.",
        "effectiveUse": "Writing assistance, code generation, tutoring, summarisation, research support.",
        "realWorldExamples": "ChatGPT, GitHub Copilot, Claude, Gemini.",
        "advantages": "Very versatile and accessible through natural language.",
        "limitations": "Hallucinations, high compute cost, outdated knowledge, imprecise logic.",
        "misuse": "Mass disinformation, phishing, academic dishonesty, malicious code generation.",
        "ethics": "Raises concerns about copyright, employment, power concentration, and environmental cost.",
        "waContext": "WA's technology sector is adopting LLMs in mining, agriculture, healthcare, and education.",
        "media": [
            {
                "id": 16,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600",
                "title": "Modern AI Interface",
                "caption": "The conversational interfaces that made LLMs accessible to everyone"
            },
            {
                "id": 17,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600",
                "title": "AI Computing Infrastructure",
                "caption": "The massive computing infrastructure required to train LLMs"
            }
        ],
        "references": [
            {
                "id": 15,
                "title": "GPT-4 Technical Report",
                "url": "https://arxiv.org/abs/2303.08774",
                "sourceType": "Research Paper",
                "accessedDate": "2024-03-20",
                "notes": "OpenAI's technical report on GPT-4"
            },
            {
                "id": 16,
                "title": "On the Dangers of Stochastic Parrots",
                "url": "https://dl.acm.org/doi/10.1145/3442188.3445922",
                "sourceType": "Research Paper",
                "accessedDate": "2024-03-20",
                "notes": "Bender et al.'s critique of LLMs"
            }
        ]
    }
]



def seed_database():
    with app.app_context():

        print("Seeding / Updating topics...")

        for topic_data in TOPICS_DATA:

            # -------------------------
            # CHECK IF EXISTS (by slug)
            # -------------------------
            topic = Topic.query.filter_by(slug=topic_data["slug"]).first()

            if topic:
                # -------------------------
                # UPDATE EXISTING
                # -------------------------
                topic.title = topic_data["title"]
                topic.year_range = topic_data["yearRange"]
                topic.category = topic_data["category"]
                topic.status = topic_data["status"]
                topic.intro_text = topic_data["introText"]
                topic.short_summary = topic_data["shortSummary"]
                topic.how_it_works = topic_data["howItWorks"]
                topic.simple_example = topic_data["simpleExample"]
                topic.effective_use = topic_data["effectiveUse"]
                topic.real_world_examples = topic_data["realWorldExamples"]
                topic.advantages = topic_data["advantages"]
                topic.limitations = topic_data["limitations"]
                topic.misuse = topic_data["misuse"]
                topic.ethics = topic_data["ethics"]
                topic.wa_context = topic_data["waContext"]

                print(f"Updated: {topic.slug}")

            else:
                # -------------------------
                # CREATE NEW
                # -------------------------
                topic = Topic(
                    slug=topic_data["slug"],
                    title=topic_data["title"],
                    year_range=topic_data["yearRange"],
                    category=topic_data["category"],
                    status=topic_data["status"],
                    intro_text=topic_data["introText"],
                    short_summary=topic_data["shortSummary"],
                    how_it_works=topic_data["howItWorks"],
                    simple_example=topic_data["simpleExample"],
                    effective_use=topic_data["effectiveUse"],
                    real_world_examples=topic_data["realWorldExamples"],
                    advantages=topic_data["advantages"],
                    limitations=topic_data["limitations"],
                    misuse=topic_data["misuse"],
                    ethics=topic_data["ethics"],
                    wa_context=topic_data["waContext"],
                )

                db.session.add(topic)
                db.session.flush()

                print(f"Created: {topic.slug}")

            # -------------------------
            # CLEAR OLD MEDIA/REFERENCES
            # -------------------------
            Media.query.filter_by(topic_id=topic.id).delete()
            TopicReference.query.filter_by(topic_id=topic.id).delete()

            # -------------------------
            # ADD MEDIA
            # -------------------------
            for media_data in topic_data.get("media", []):
                media = Media(
                    topic_id=topic.id,
                    type=media_data["type"],
                    title=media_data["title"],
                    url=media_data["url"],
                    caption=media_data["caption"],
                )
                db.session.add(media)

            # -------------------------
            # ADD REFERENCES
            # -------------------------
            for ref_data in topic_data.get("references", []):
                reference = TopicReference(
                    topic_id=topic.id,
                    title=ref_data["title"],
                    url=ref_data["url"],
                    source_type=ref_data["sourceType"],
                    accessed_date=ref_data["accessedDate"],
                    notes=ref_data["notes"],
                )
                db.session.add(reference)

        db.session.commit()
        print("Database updated successfully!")


if __name__ == "__main__":
    seed_database()