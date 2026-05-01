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
        "introText": "Expert systems were one of the most important symbolic AI technologies of the 1980s. They were designed to imitate the decision-making ability of a human expert in a narrow domain by storing specialist knowledge in rules and facts.",
        "shortSummary": "Expert systems captured human specialist knowledge in rule-based software, allowing computers to provide recommendations and decisions in domains such as medicine, troubleshooting, finance, and industry.",
        "howItWorks": "An expert system usually consists of a knowledge base, an inference engine, and a user interface. Knowledge is stored as facts, relationships, and if-then-else rules. The inference engine applies these rules step by step to reach a conclusion. Two common reasoning methods are forward chaining, which starts from known facts and moves toward a conclusion, and backward chaining, which starts from a possible conclusion and checks whether the supporting facts are true.",
        "simpleExample": "Imagine a car fault diagnosis system. If the engine does not start and the battery lights are weak, the system may conclude that the battery is flat and recommend recharging or replacing it. In a more advanced example such as MYCIN, the system used rules about symptoms, infections, and treatments to recommend antibiotics.",
        "effectiveUse": "Most effective in narrow, stable, and rule-based domains where specialist knowledge can be clearly expressed, such as medical diagnosis, troubleshooting, legal reasoning, financial advice, and industrial monitoring.",
        "realWorldExamples": "Classic examples include MYCIN for medical diagnosis and antibiotic recommendation, DENDRAL for chemical analysis, and XCON for computer system configuration.",
        "advantages": "Expert systems can preserve specialist knowledge, provide consistent decisions, and support fast decision-making in repetitive or highly specialised tasks. They do not become tired and can continue to apply the same logic reliably.",
        "limitations": "Their performance depends heavily on the quality of the knowledge base. They are difficult to build and maintain, often suffer from the knowledge acquisition bottleneck, and usually work only in narrow domains. They also struggle with ambiguity and unfamiliar situations.",
        "misuse": "They can be misused when applied outside their intended domain, or when users trust outdated, incomplete, or biased rules too much in high-stakes areas such as medicine, law, or finance.",
        "ethics": "Important concerns include accountability, transparency, and over-reliance. Some expert systems also used Bayes theorem to reason under uncertainty and fuzzy logic to handle vague concepts, but even then the system’s outputs could still create risks if human judgement was ignored.",
        "waContext": "In Western Australia, expert-system and rule-based decision support approaches were relevant in industrial environments such as Alcoa’s Wagerup alumina refinery, where expert knowledge could support diagnostics, scheduling, and operational planning.",
        "media": [
            {
                "id": 5,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=1200&q=80",
                "title": "Knowledge Engineering in Practice",
                "caption": "Expert systems translated specialist knowledge into structured rules for decision support."
            },
            {
                "id": 4,
                "type": "image",
                "url": "/static/images/expert-systems-diagram.png",
                "title": "Basic Structure of an Expert System",
                "caption": "A simplified expert system structure showing the knowledge base, inference engine, user interface, and external data sources."
            }
        ],
        "references": [
            {
                "id": 4,
                "title": "Wagerup Alumina Refinery Long Term Residue Management Strategy",
                "url": "https://www.alcoa.com/australia/en/pdf/2017-wagerup-refinery-ltrms.pdf",
                "sourceType": "Industry Report",
                "accessedDate": "Accessed 2026",
                "notes": "WA-based industrial context showing the relevance of expert knowledge and decision support in large-scale operations."
            },
            {
                "id": 5,
                "title": "Expert Systems",
                "url": "https://en.wikipedia.org/wiki/Expert_system",
                "sourceType": "Background Source",
                "accessedDate": "Accessed 2026",
                "notes": "General overview of knowledge bases, inference engines, and classic expert-system applications."
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
        "introText": "Evolutionary computing is a branch of artificial intelligence inspired by biological evolution. One of its best-known techniques is the genetic algorithm, which searches for strong solutions by imitating natural selection, reproduction, and mutation.",
        "shortSummary": "Genetic algorithms solve complex optimisation and search problems by evolving a population of candidate solutions over many generations using selection, crossover, and mutation.",
        "howItWorks": "A genetic algorithm begins with a population of candidate solutions. Each candidate is evaluated using a fitness function that measures how well it solves the problem. Better candidates are more likely to be selected to form the next generation. New candidates are produced through crossover, which combines features of parent solutions, and mutation, which introduces small random changes. Over time, the population tends to improve, although the algorithm may still converge to a strong local optimum rather than the global optimum.",
        "simpleExample": "A delivery company may want to find a short route for a truck visiting many locations. A genetic algorithm can begin with many random route candidates, score them by total distance, and then repeatedly select, combine, and mutate the best candidate solutions. The algorithm mutates the encoded candidate solutions, not the real-world route data itself.",
        "effectiveUse": "Most effective when a problem has a very large search space, many possible combinations, or conflicting objectives. It is often used in optimisation, scheduling, engineering design, logistics, machine learning, and feature selection.",
        "realWorldExamples": "Applications include route planning, scheduling, engineering optimisation, machine learning feature selection, and other search problems where traditional mathematical optimisation is too rigid or expensive.",
        "advantages": "Genetic algorithms can examine very large numbers of candidate solutions, avoid some of the limits of human intuition, and discover non-obvious or creative solutions in highly complex search spaces.",
        "limitations": "They do not guarantee the global optimum, and their effectiveness depends heavily on the encoding method, fitness function, and parameter settings such as mutation rate, crossover rate, and population size. They can also be computationally expensive.",
        "misuse": "They can produce harmful results if the fitness function is poorly designed, for example by optimising only cost or efficiency while ignoring fairness, safety, or environmental consequences.",
        "ethics": "Important concerns include accountability, over-reliance, and the risk of optimising the wrong objective. A mathematically efficient result may still be socially harmful if human values are not reflected in the design.",
        "waContext": "In Western Australia, UWA researchers applied problem-specific genetic algorithms to optimise sparse power distribution network planning in the South-West, and also explored multi-objective genetic algorithm optimisation for road network widening and maintenance scheduling.",
        "media": [
            {
                "id": 11,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1500462918059-b1a0cb512f1d?w=600",
                "title": "Bio-Inspired Optimisation",
                "caption": "Evolutionary computing drew inspiration from natural selection to solve complex optimisation problems."
            },
            {
                "id": 10,
                "type": "image",
                "url": "/static/images/genetic-algorithm-flowchart.png",
                "title": "Genetic Algorithm Flow",
                "caption": "A simplified flowchart showing initial population, selection, mating, crossover, mutation, and termination."
            }
        ],
        "references": [
            {
                "id": 9,
                "title": "Spatial Optimisation for the Planning of Sparse Power Distribution Networks",
                "url": "https://doi.org/10.1109/TPWRS.2018.2846407",
                "sourceType": "Research Paper",
                "accessedDate": "Accessed 2026",
                "notes": "UWA-related WA application of optimisation methods in regional power distribution planning."
            },
            {
                "id": 10,
                "title": "Genetic Algorithms Short Tutorial",
                "url": "https://www.cs.ucdavis.edu/~vemuri/classes/ecs271/Genetic%20Algorithms%20Short%20Tutorial.htm",
                "sourceType": "Tutorial",
                "accessedDate": "Accessed 2026",
                "notes": "Accessible explanation of the stages of a genetic algorithm and its optimisation cycle."
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