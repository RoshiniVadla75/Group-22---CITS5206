from app import app
from models import db, Topic, Media, TopicReference


TOPICS_DATA = [
    {
        "id": 1,
        "slug": "turing-thoughts-on-ai",
        "title": "Alan Turing & The Turing Test",
        "yearRange": "c. 1950",
        "category": "Foundations",
        "status": "Legacy",
        "introText": "Alan Turing was one of the earliest thinkers to explore artificial intelligence. His idea of the Turing Test evaluates machine intelligence based on behaviour rather than internal structure.",
        "shortSummary": "The Turing Test evaluates whether a machine can exhibit human-like behaviour through conversation.",
        "howItWorks": "Turing proposed that machines could produce intelligent behaviour by following logical rules and algorithms rather than copying the human brain. Systems can simulate reasoning and decision-making by evaluating options and selecting the most favourable outcomes, such as in a chess game.",
        "simpleExample": "A machine playing chess evaluates possible moves and selects the best option based on defined criteria. Another example is ELIZA, a program from the 1960s that simulated conversation using pattern-matching rules, showing how machines can appear intelligent without true understanding.",
        "effectiveUse": "Evaluating conversational systems, game-playing AI, and decision-making systems based on observable behaviour.",
        "realWorldExamples": "Chatbots, conversational agents, large language models, game-playing systems, and decision-support tools.",
        "advantages": "Focuses on observable behaviour, provides a practical evaluation method, and encourages human-like interaction in AI systems.",
        "limitations": "Passing the Turing Test does not imply true understanding. It focuses mainly on conversation and depends on subjective human judgement.",
        "misuse": "Can be misused in systems that imitate humans to deceive users, generate misleading information, or manipulate users.",
        "ethics": "Raises concerns about trust, transparency, deception, and responsible use of human-like AI systems.",
        "waContext": "In Western Australia, Turing’s ideas influence conversational systems and automated support tools used in customer service, digital platforms, and universities. This influence is also linked to Professor Jeff Rohl at UWA, who worked at the University of Manchester shortly after Turing’s time. Behaviour-based evaluation remains important in modern AI systems across WA.",
        "media": [
            {
                "id": 1,
                "type": "image",
                "url": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Alan_Turing_Aged_16.jpg",
                "title": "Alan Turing",
                "caption": "Alan Turing, a pioneer of artificial intelligence and the originator of the Turing Test"
            }
        ],
        "references": [
            {
                "id": 1,
                "title": "Artificial neural networks technology",
                "url": "https://d1wqtxts1xzle7.cloudfront.net/33786328/Artificial_Neural_Networks_Technology-libre.pdf",
                "sourceType": "Research Paper",
                "accessedDate": "2026",
                "notes": "Anderson & McNeill (1992)"
            },
            {
                "id": 2,
                "title": "Artificial neural networks: fundamentals, computing, design, and application",
                "url": "https://nathan.instras.com/ResearchProposalDB/doc-7.pdf",
                "sourceType": "Research Paper",
                "accessedDate": "2026",
                "notes": "Basheer & Hajmeer (2000)"
            },
            {
                "id": 3,
                "title": "Artificial neural networks for beginners",
                "url": "https://arxiv.org/pdf/cs/0308031",
                "sourceType": "Research Paper",
                "accessedDate": "2026",
                "notes": "Gershenson (2003)"
            },
            {
                "id": 4,
                "title": "Fundamentals of artificial neural networks",
                "url": "https://www.researchgate.net/profile/Terrence-Fine/publication/3078997_Fundamentals_of_Artificial_Neural_Networks-Book_Reviews",
                "sourceType": "Book",
                "accessedDate": "2026",
                "notes": "Hassoun (1995)"
            },
            {
                "id": 5,
                "title": "What are artificial neural networks?",
                "url": "http://www.lmse.org/assets/learning/bioinformatics/Reading/Krogh2008NatureBiotech_ANN.pdf",
                "sourceType": "Research Paper",
                "accessedDate": "2026",
                "notes": "Krogh (2008)"
            }
        ]
    },
    {
        "id": 2,
        "slug": "learning-machines",
        "title": "Learning Machines",
        "yearRange": "1950s–1980s",
        "category": "Machine Learning",
        "status": "Legacy",
        "introText": "Learning machines represent an early shift in artificial intelligence from fixed, rule-based systems to systems that improve through experience. Instead of relying solely on predefined instructions, these systems incorporate feedback mechanisms, allowing behaviour to change based on performance over time. A key example is the work of Arthur Samuel, who developed a checkers program that improved through self-play. The program evaluated board positions using a scoring function and updated this function based on game outcomes. This demonstrated that a machine could refine its behaviour without explicit reprogramming, reaching strategies not directly anticipated by its designer. During the 1950s to 1980s, this idea of feedback-driven improvement became central to early machine learning. Systems in this period were typically simple in structure but introduced the important concept of adaptive algorithms, where performance improves through repeated evaluation and adjustment.",
        "shortSummary": "Learning machines introduced adaptive behaviour by using feedback-driven improvement. A system generates an action, evaluates the result, updates its parameters, and repeats the process.",
        "howItWorks": "A learning machine operates through a cycle of action, evaluation, and adjustment. This process involves generating an action based on current parameters, evaluating the result using a scoring or utility function, and updating parameters to improve future outcomes. In Samuel’s checkers program, this formed a self-play feedback loop, where the system repeatedly played games against itself and refined its evaluation function based on success or failure. Unlike later machine learning systems, early learning machines relied on explicitly defined features and relatively simple update rules. Their importance lies in introducing adaptive behaviour rather than architectural complexity. This process forms a feedback loop, where the system continuously improves its performance through repeated cycles of evaluation and adjustment.",
        "simpleExample": "A checkers program evaluates board states using features such as piece count and positional strength. Each feature has an associated weight. After repeated games, the system adjusts these weights to favour strategies associated with winning outcomes. Another example is early optimisation systems that adjust parameters to reduce prediction error. These systems compare predicted outcomes with observed results and iteratively update parameters to improve accuracy.",
        "effectiveUse": "The principles established by early learning machines underpin many modern systems. Applications include optimisation problems where parameters are refined iteratively, recommendation systems that adapt to user behaviour, and adaptive control systems in engineering. Although modern systems are more complex, they continue to rely on feedback-driven improvement, which originates from early learning machine research.",
        "realWorldExamples": "Samuel’s checkers program remains a defining example of a learning machine. Through self-play and iterative adjustment, the system improved its performance beyond its initial configuration, demonstrating that behaviour could emerge from experience rather than fixed rules.",
        "advantages": "Learning machines enable systems to improve without manual reprogramming, adapt to changing data and environments, and form the foundation of modern machine learning.",
        "limitations": "Learning machines depend on the quality of feedback data. Early systems required carefully designed features, and learning processes may converge slowly or to suboptimal results.",
        "misuse": "Learning systems may reinforce biased or incorrect patterns if training data or feedback signals are flawed. This can lead to unintended or misleading outcomes.",
        "ethics": "Learning machines optimise measurable objectives, which may not align with broader social or ethical goals. Oversight is required to ensure responsible use and to manage risks related to bias and unintended behaviour.",
        "waContext": "In Western Australia, the influence of learning machines is reflected in research, infrastructure, and industrial application. The University of Western Australia conducts teaching and research in machine learning, data science, and optimisation. These areas build on the principles of adaptive systems and iterative improvement. The Pawsey Supercomputing Research Centre, located in Perth, provides high-performance computing infrastructure that supports large-scale data processing and model training. This infrastructure enables modern systems that extend early learning machine concepts. In industry, Rio Tinto applies machine learning techniques in areas such as predictive maintenance and operational optimisation, where systems improve performance using historical data.",
        "media": [
            {
                "id": 2,
                "type": "image",
                "url": "/static/images/learning-machines-feedback-loop.png",
                "title": "Learning Machine Feedback Loop",
                "caption": "Figure 1. A simplified feedback loop in a learning machine, showing how a system generates an action, evaluates the outcome, updates its parameters, and repeats the process. Source: Author’s own diagram, based on Samuel (1959)."
            },
            {
                "id": 20,
                "type": "image",
                "url": "/static/images/pawsey-supercomputing-centre.png",
                "title": "Pawsey Supercomputing Research Centre",
                "caption": "Figure 2. Pawsey Supercomputing Research Centre in Western Australia, supporting large-scale computational research."
            }
        ],
        "references": [
            {
                "id": 2,
                "title": "Some studies in machine learning using the game of checkers",
                "url": "https://doi.org/10.1147/rd.33.0210",
                "sourceType": "Research Paper",
                "accessedDate": "Accessed 2026",
                "notes": "Samuel, A. L. (1959). IBM Journal of Research and Development, 3(3), 210–229."
            },
            {
                "id": 20,
                "title": "Data science at UWA",
                "url": "https://www.uwa.edu.au/projects/data-science-at-uwa",
                "sourceType": "University Website",
                "accessedDate": "Accessed 2026",
                "notes": "The University of Western Australia. (2024, November 27)."
            },
            {
                "id": 21,
                "title": "Pawsey Supercomputing Research Centre",
                "url": "https://www.csiro.au/en/about/facilities-collections/pawsey-supercomputing-research-centre",
                "sourceType": "Research Infrastructure Website",
                "accessedDate": "Accessed 2026",
                "notes": "CSIRO. (2023)."
            },
            {
                "id": 22,
                "title": "Using AI and data science for better operations",
                "url": "https://www.riotinto.com/en/news/stories/using-ai-data-science-for-better-operations",
                "sourceType": "Industry Website",
                "accessedDate": "Accessed 2026",
                "notes": "Rio Tinto. (2024)."
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
    "introText": "Artificial Neural Networks (ANNs) are inspired by the structure of the human brain and learn patterns from data through interconnected neurons.",
    "shortSummary": "ANNs learn complex patterns through layered structures and form the foundation of modern deep learning systems.",
    "howItWorks": "ANNs consist of an input layer, one or more hidden layers, and an output layer. Data is passed through the network, where each neuron applies weighted calculations. During training, the system adjusts these weights to reduce error and improve performance. Deep learning extends this by using multiple hidden layers to capture more complex relationships in data.",
    "simpleExample": "An image classification system processes pixel data through multiple layers to detect features such as edges, shapes, and colours, and then predicts whether the image is a cat or a dog.",
    "effectiveUse": "Pattern recognition tasks such as image classification, speech recognition, and data analysis.",
    "realWorldExamples": "Facial recognition systems, handwriting recognition, speech recognition, medical diagnosis, and financial prediction.",
    "advantages": "They can learn directly from data, model complex relationships, detect hidden patterns, and improve performance with more data.",
    "limitations": "Training requires large datasets and computational resources. The internal decision-making process is often difficult to interpret, leading to 'black box' concerns.",
    "misuse": "ANNs can be misused in surveillance systems, biased automated decision-making, and misleading predictive systems.",
    "ethics": "Key concerns include bias in training data, lack of transparency, and fairness in automated decision-making.",
    "waContext": "In Western Australia, neural network research is mainly carried out in universities and research institutions such as UWA, Curtin, ECU, and Murdoch University, as well as organisations like CSIRO. Facilities such as the Pawsey Supercomputing Research Centre support large-scale data processing and AI research. Neural networks are also applied in projects like the Square Kilometre Array (SKA) to analyse large volumes of scientific data.",
    "media": [
        {
            "id": 6,
            "type": "image",
            "url": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600",
            "title": "Neural Network Architecture",
            "caption": "Basic structure of an artificial neural network with input, hidden, and output layers"
        },
        {
            "id": 7,
            "type": "image",
            "url": "https://images.unsplash.com/photo-1559757175-5700dde675bc?w=600",
            "title": "Brain-Inspired Computing",
            "caption": "Neural networks are inspired by the structure of the human brain"
        }
    ],
    "references": [
        {
            "id": 5,
            "title": "Artificial neural networks: fundamentals, computing, design, and application",
            "url": "https://nathan.instras.com/ResearchProposalDB/doc-7.pdf",
            "sourceType": "Research Paper",
            "accessedDate": "2026",
            "notes": "Basheer & Hajmeer (2000)"
        },
        {
            "id": 6,
            "title": "Artificial neural networks for beginners",
            "url": "https://arxiv.org/pdf/cs/0308031",
            "sourceType": "Research Paper",
            "accessedDate": "2026",
            "notes": "Gershenson (2003)"
        },
        {
            "id": 7,
            "title": "Fundamentals of artificial neural networks",
            "url": "https://www.researchgate.net/profile/Terrence-Fine/publication/3078997_Fundamentals_of_Artificial_Neural_Networks-Book_Reviews/links/56ebf73a08aee4707a3849a6/Fundamentals-of-Artificial-Neural-Networks-Book-Reviews.pdf",
            "sourceType": "Book",
            "accessedDate": "2026",
            "notes": "Hassoun (1995)"
        },
        {
            "id": 8,
            "title": "What are artificial neural networks?",
            "url": "http://www.lmse.org/assets/learning/bioinformatics/Reading/Krogh2008NatureBiotech_ANN.pdf",
            "sourceType": "Research Paper",
            "accessedDate": "2026",
            "notes": "Krogh (2008)"
        },
        {
            "id": 9,
            "title": "Perceptrons: An Introduction to Computational Geometry",
            "url": "https://mitpress.mit.edu/9780262630229/perceptrons/",
            "sourceType": "Book",
            "accessedDate": "2026",
            "notes": "Minsky & Papert (1969)"
        }
    ]
},
    {
        "id": 6,
        "slug": "internet-driven-ai-ibm-watson",
        "title": "Internet-Driven AI Systems",
        "yearRange": "c. 2011",
        "category": "Knowledge Retrieval",
        "status": "Legacy",
        "introText": "With the growth of the internet, AI systems gained access to large-scale data, enabling them to connect information across sources and simulate general knowledge.",
        "shortSummary": "Internet-driven AI systems retrieve, evaluate, and rank information from large datasets rather than relying on fixed rules.",
        "howItWorks": "Internet-driven AI systems process large amounts of unstructured data such as web pages, documents, and databases. They convert text using NLP techniques, generate multiple candidate answers, and evaluate them using evidence. A key step is 'soft filtering', where less likely answers are gradually removed based on confidence scores rather than strict rules. Systems such as IBM Watson use architectures like DeepQA to rank answers and select the most probable result.",
        "simpleExample": "For example, when asked 'Who is the president of the United States?', the system searches large datasets, identifies patterns linking names with that role, and selects the most likely answer. In quiz-style tasks such as Jeopardy!, the system analyses clues, gathers evidence, and ranks competing answers.",
        "effectiveUse": "Question answering, search engines, virtual assistants, and knowledge retrieval systems that require analysing large amounts of data quickly.",
        "realWorldExamples": "IBM Watson, Jeopardy!, search engines, virtual assistants, enterprise knowledge systems, and data-driven decision support tools.",
        "advantages": "They can access large amounts of information, connect knowledge from multiple sources, provide fast responses, and improve as more data becomes available.",
        "limitations": "They depend on data quality, require significant computational resources, and rely on statistical patterns rather than true understanding, which can lead to incorrect or misleading results.",
        "misuse": "Can be misused to spread misinformation, generate misleading answers, and manipulate information at scale.",
        "ethics": "Key concerns include reliability of sources, bias in data, and over-reliance on automated decision-making systems.",
        "waContext": "In Western Australia, internet-driven AI systems are widely used in industries such as mining and energy. Companies like Rio Tinto and BHP use data-driven systems and remote operations centres to monitor and manage large-scale operations. Universities such as UWA and Curtin also contribute to research in information retrieval and large-scale data analysis.",
        "media": [
            {
                "id": 8,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=600",
                "title": "Internet-Driven AI Process",
                "caption": "Simplified process of an internet-driven AI system such as IBM Watson for question answering"
            },
            {
                "id": 9,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600",
                "title": "Data-Driven AI in Western Australia",
                "caption": "Large-scale data systems supporting decision-making in WA industries"
            }
        ],
        "references": [
            {
                "id": 7,
                "title": "Building Watson: An overview of the DeepQA project",
                "url": "https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2303",
                "sourceType": "Research Paper",
                "accessedDate": "2026",
                "notes": "Ferrucci et al. (2010)"
            },
            {
                "id": 8,
                "title": "Introduction to 'This is Watson'",
                "url": "https://ieeexplore.ieee.org/abstract/document/6177724",
                "sourceType": "Research Paper",
                "accessedDate": "2026",
                "notes": "Ferrucci (2012)"
            },
            {
                "id": 9,
                "title": "Question analysis: How Watson reads a clue",
                "url": "https://www.patwardhans.net/papers/LallyEtAl12.pdf",
                "sourceType": "Research Paper",
                "accessedDate": "2026",
                "notes": "Lally et al. (2012)"
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
        "introText": "Synthetic Media Technologies use neural networks to create highly realistic fake media.",
        "shortSummary": "Synthetic Media Technologies, commonly referred to as Deep fakes use deep learning - specifically Generative Adversarial Networks (GANs) - to synthesise realistic but fabricated images, videos, and audio of real people. Emerging around 2015, they represent one of the most ethically complex and socially disruptive AI technologies.",
        "howItWorks": "A GAN consists of two competing neural networks: a Generator (which creates fake content) and a Discriminator (which tries to detect fakes). The two networks train together: the generator improves at creating convincing fakes; the discriminator improves at detecting them. Over time, the generator produces increasingly realistic synthetic media. Deep fakes additionally use face-swapping techniques (autoencoders and facial landmark detection) to map one person’s face onto another’s with high fidelity.",
        "simpleExample": "Start with thousands of photos of Person A and video footage of Person B. The GAN learns the facial geometry, lighting, and expression patterns of Person A. It then replaces Person B’s face in the video with a photorealistic rendering of Person A’s face, frame by  frame - resulting in a convincing video of Person A saying things they never said or doing things they never did.",
        "effectiveUse": "Deep fake technology has legitimate applications in film production (de ageing actors, dubbing into other languages while preserving lip sync), gaming (realistic character animation), accessibility (generating synthetic voices for people who have lost theirs), and historical preservation (animating archival photographs).",
        "realWorldExamples": "Hollywood studios use deep fake technology to de-age actors. The Dali Museum recreated Salvador Dali using deep fakes for interactive exhibitions. Ukraine’s president was targeted by a deep fake video urging troops to surrender. The eSafety Commissioner identifies deep fakes as a growing risk for identity theft, humiliation, extortion, sexual exploitation, and reputational damage.",
        "advantages": "Deep-fake systems can generate or alter media at a scale and speed impossible for manual editing alone. They can automate detailed synthesis, imitate facial or vocal patterns quickly, and create many variations of a scene far faster than a human editor working frame by frame.",
        "limitations": "Deep fakes can still be detected by artefacts around eyes, ears, and hair, and by unnatural blinking or lighting. They require significant compute and data for high quality. Real-time deep fakes at high resolution remain challenging. Detection tools are in an arms race with generation tools",
        "misuse": "Deep fakes are weaponised for political disinformation, fraud (CEO voice spoofing for wire transfers), non-consensual intimate imagery, reputation destruction, and evidence fabrication. They fundamentally undermine trust in audiovisual evidence - the concept of ‘seeing is believing.’ ",
        "ethics": "Deep fakes attack foundational concepts of truth, consent, and identity. They can cause severe psychological harm to victims of non-consensual synthetic imagery. They create an epistemic crisis in democratic societies where shared visual reality is a basis for public discourse. Legal frameworks are struggling to keep pace.",
        "waContext": "Western Australia’s involvement in synthetic media technologies is based on existing expertise in computer vision and AI research, combined with national-level regulation and response systems. At WA universities such as Curtin University and University of Western Australia, research in: image analysis, machine learning, pattern recognition - forms the technical foundation used in deepfake detection and analysis. These capabilities are directly linked to synthetic media systems, which rely on similar techniques for generating and identifying manipulated content.At the national level, Australia’s eSafety Commissioner  has formally identified deepfakes as a significant emerging risk, including: identity misuse, misinformation, reputational harm. This is supported by active regulatory frameworks, including: reporting systems for harmful content, enforcement mechanisms, public awareness initiatives.These policies directly influence how WA addresses synthetic media through education and digital literacy programs",
        "media": [
            {
                "id": 12,
                "type": "image",
                "url": "/static/images/deep%20fake.png",
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
                "title": "Generative Adversarial Nets",
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
            },
            {
                "id": 13,
                "title": "Deepfakes and Manipulated Media",
                "url": "https://www.esafety.gov.au/",
                "sourceType": "Government Website",
                "accessedDate": "2026-03-23",
                "notes": "eSafety Commissioner guidance on deepfakes"
            },
            {
                "id": 14,
                "title": "Generative Adversarial Nets",
                "url": "N/A",
                "sourceType": "Journal Article",
                "accessedDate": "2026-03-23",
                "notes": "Goodfellow, I., Pouget-Abadie, J., & Mirza, M. (2014). Advances in Neural Information Processing Systems, 2672-2680"
            },
            {
                "id": 15,
                "title": "Deepfakes: Trick or Treat?",
                "url": "N/A",
                "sourceType": "Journal Article",
                "accessedDate": "2026-03-23",
                "notes": "Kietzmann, J., Lee, L., & McCarthy, I. (2020). Business Horizons, 63(2), 135-146"
            },
            {
                "id": 16,
                "title": "The Emergence of Deepfake Technology",
                "url": "N/A",
                "sourceType": "Journal Article",
                "accessedDate": "2026-03-23",
                "notes": "Westerlund, M. (2019). Technology Innovation Management Review, 9(11)"
            },
             {
                "id": 17,
                "title": "Deepfakes: A Looming Challenge for Privacy, Democracy, and National Security",
                "url": "N/A",
                "sourceType": "Journal Article",
                "accessedDate": "2026-03-23",
                "notes": "Citron, D., & Chesney, R. (2019). California Law Review"
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
    "introText": "Natural Language Processing (NLP) enables computers to read, “understand”, and generate human language, although this “understanding” is based on pattern analysis rather than true human comprehension.",
    "shortSummary": "NLP allows computers to process language through tokenisation, vector representations, and transformer-based models.",
    "howItWorks": "NLP systems convert human language into numerical representations that computers can process. Text is first tokenised into smaller units such as words or subwords, then converted into vectors that capture relationships between words. Modern NLP systems, especially transformer models, use attention mechanisms to process context and relationships between words. Importantly, these systems do not truly understand language in the human sense; instead, they identify patterns such as nouns, verbs, and sentence structure, and generate outputs based on statistical relationships learned from data.",
    "simpleExample": "For example, in the sentence 'book a flight to Sydney tomorrow', the system tokenises the text, converts it into vectors, identifies patterns suggesting the user’s intent, and extracts information such as destination and time to generate an appropriate action.",
    "effectiveUse": "Machine translation, summarisation, question answering, sentiment analysis, chatbots, and information extraction.",
    "realWorldExamples": "Speech recognition, machine translation, sentiment analysis, chatbots, search engines, customer support systems, and transformer-based models such as BERT and GPT.",
    "advantages": "NLP systems can process large amounts of text quickly, operate continuously without fatigue, and automate repetitive language tasks. Transformer models are flexible and can be adapted to many real-world applications.",
    "limitations": "Human language is complex and context-dependent, making full understanding difficult. NLP systems rely on statistical patterns rather than true comprehension, can inherit bias from training data, and often require significant computational resources.",
    "misuse": "NLP can be misused to generate fake or misleading content, automate scams or spam messages, and produce biased or harmful text.",
    "ethics": "Key ethical concerns include bias in language data, misinformation, harmful outputs, and the social impact of automated language systems.",
    "waContext": "In Western Australia, NLP research has developed mainly through universities and research institutions such as UWA, Curtin, ECU, Murdoch University, and organisations including CSIRO. Research infrastructure such as the Pawsey Supercomputing Research Centre supports large-scale NLP and AI work, while projects such as the Square Kilometre Array (SKA) highlight the role of NLP in processing textual and metadata information for scientific research.",
    "media": [
        {
            "id": 14,
            "type": "image",
            "url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600",
            "title": "Language Processing Pipeline",
            "caption": "Basic pipeline of a Natural Language Processing system"
        },
        {
            "id": 15,
            "type": "image",
            "url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600",
            "title": "Pawsey Supercomputing Research Centre",
            "caption": "Research infrastructure supporting AI and NLP work in Western Australia"
        }
    ],
    "references": [
        {
            "id": 13,
            "title": "Natural language processing",
            "url": "https://mbahng.com/Natural_Sciences/Statistics/Natural_Language_Processing/paper.pdf",
            "sourceType": "Research Paper",
            "accessedDate": "2026",
            "notes": "Bahng (2024)"
        },
        {
            "id": 14,
            "title": "Advances in natural language processing",
            "url": "https://nlp.stanford.edu/~manning/xyzzy/Hirschberg-Manning-Science-2015.pdf",
            "sourceType": "Research Paper",
            "accessedDate": "2026",
            "notes": "Hirschberg & Manning (2015)"
        },
        {
            "id": 15,
            "title": "Natural language processing: A historical review",
            "url": "https://aclanthology.org/www.mt-archive.info/90/Zampolli-1994-Sparck-Jones.pdf",
            "sourceType": "Book Chapter",
            "accessedDate": "2026",
            "notes": "Sparck Jones (1994)"
        },
        {
            "id": 16,
            "title": "Transformers: State-of-the-art natural language processing",
            "url": "https://aclanthology.org/2020.emnlp-demos.6.pdf",
            "sourceType": "Conference Paper",
            "accessedDate": "2026",
            "notes": "Wolf et al. (2020)"
        },
        {
            "id": 17,
            "title": "Survey of transformers and towards ensemble learning using transformers for natural language processing",
            "url": "https://link.springer.com/content/pdf/10.1186/s40537-023-00842-0.pdf",
            "sourceType": "Research Paper",
            "accessedDate": "2026",
            "notes": "Zhang & Shafiq (2024)"
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
        "shortSummary": "Large Language Models (LLMs) like GPT-4, Claude, Gemini, and Llama represent the cutting edge of AI in 2024. Trained on trillions of words and hundreds of billions of parameters, they exhibit capabilities by performing tasks they were never explicitly trained for and are transforming every industry.",
        "howItWorks": "LLMs are extremely large transformer neural networks trained on vast internet text using self-supervised learning (predicting the next word). Their scale creates emergent capabilities: reasoning, code generation, instruction following, translation, mathematics, and creative writing - all from the same model. Reinforcement learning from Human Feedback (RLHF) is used to align model outputs with human preferences and safety guidelines. Models are accessed via Application Programming Interfaces (APIs) or run locally on consumer hardware.",
        "simpleExample": "Ask an LLM: ‘Explain quantum entanglement to a 10-year-old using a story about socks.’ The model has never seen that exact prompt but draws on its training to craft an age-appropriate metaphor, with narrative structure and accurate physics - an example of generalisation for beyond simple pattern matching.",
        "effectiveUse": "LLMs are most effective as flexible general-purpose assistants for text generation, code writing, summarisation, Q&A, translation, tutoring, creative writing, and data analysis. They are transforming software development, education, legal research, scientific writing, and customer service",
        "realWorldExamples": "ChatGPT (OpenAI) reached 100 million users in two months – the fastest growing consumer application in history. GitHub Copilot, powered by OpenAI, assists millions of developers with code. Claude (Anthropic) is used for long-form document analysis. Google Gemini integrates into Google Workspace. Meta’s Llama models enable open-source deployment on consumer hardware.",
        "advantages": "LLMs can process and generate text at a speed and scale that humans cannot match. They can draft multiple versions of a response quickly, work across many subject areas, and handle large volumes of text without fatigue. In educational settings, they can provide immediate feedback and different levels of explanation, which can be useful when supervised carefully.",
        "limitations": "LLMs do not truly understand meaning in the human sense. They can hallucinate - generating confident, fluent, but factually wrong information. They have knowledge cutoffs and cannot access real-time information without tools. They can be inconsistent across sessions. Very large models require enormous compute resources. Fine-tuned alignment is imperfect; models can still harmful outputs. ",
        "misuse": "Because they produce persuasive text quickly, LLMs can be misused for disinformation, phishing messages, spam, academic misconduct, or the generation of misleading summaries that appear confident but are wrong. Their ease of use lowers the barrier for harmful content creation. ",
        "ethics": "Key ethical issues include copyright, privacy, embedded social bias, over-reliance by students, and the risk that confident machine output may be trusted without verification. For a museum or school audience, the most important message is that LLM output should be treated as a draft or assistant, not as unquestionable truth. Human checking remains essential. ",
        "waContext": "Western Australia’s capability in Large Language Models has developed through documented academic research and applied system development, rather than creating foundational models. At the University of Western Australia, researchers have directly contributed to LLM knowledge through peer-reviewed work such as “A Comprehensive Overview of Large Language Models” (2025), which surveys advanced topics including multimodal LLMs, training strategies, and benchmarking​ (University of Western Australia, 2025)​ . This shows that WA researchers are actively contributing to the global understanding and refinement of LLM systems, not just using them. At Curtin University, current research projects explicitly focus on LLM-powered autonomous systems, where language models are integrated with real-world tools such as sensors and infrastructure monitoring systems​ (Curtin University, 2025)​ . These projects demonstrate practical implementation of LLMs in areas like: infrastructure management, real-time decision systems, intelligent automation. At the national level, evidence shows that Australia does not yet produce globally competitive LLMs (like GPT-4) and instead relies on international models while focusing on application and adaptation . ",
        "media": [
            {
                "id": 16,
                "type": "image",    
                "url": "/static/images/large%20language%20models.png",
                "title": "LLM Architectures,Training, and Applications",
                "caption": "AI architectures, training processes, and applications of LLMs in various industries"
            },
            {
                "id": 17,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600",
                "title": "Modern AI Interface",
                "caption": "The conversational interfaces that made LLMs accessible to everyone"
            },
            {
                "id": 18,
                "type": "image",
                "url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600",
                "title": "AI Computing Infrastructure",
                "caption": "The massive computing infrastructure required to train LLMs"
            }
        ],
        "references": 
        [
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
            },
            {
                "id": 18,
                "title": "Large Language Models: Guidance of the WA Public Sector",
                "url": "https://www.wa.gov.au/system/files/2025-02/largelanguagemodels.pdf",
                "sourceType": "Government Report",
                "accessedDate": "2026-03-13",
                "notes": "Guidelines from WA Government on LLM usage in the public sector"
            },
            {
                "id": 19,
                "title": "Guidance on Privacy and AI Products",
                "url": "https://www.oaic.gov.au/",
                "sourceType": "Government Website",
                "accessedDate": "2026-03-24",
                "notes": "Privacy guidance for AI systems from OAIC"
            },
            {
                "id": 20,
                "title": "GPT-4 Technical Report",
                "url": "https://arxiv.org/pdf/2303.08774",
                "sourceType": "Research Paper",
                "accessedDate": "2026-03-22",
                "notes": "OpenAI's technical report on GPT-4"
            },
            {
                "id": 21,
                "title": "Training Language Models to Follow Instructions with Human Feedback",
                "url": "https://arxiv.org/pdf/2203.02155",
                "sourceType": "Research Paper",
                "accessedDate": "2026-03-22",
                "notes": "Ouyang et al. paper on RLHF for LLM alignment"
            },
            {
                "id": 22,
                "title": "Attention Is All You Need",
                "url": "https://arxiv.org/abs/1706.03762",
                "sourceType": "Research Paper",
                "accessedDate": "2026-03-22",
                "notes": "Foundational Transformer architecture paper"
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
    with app.app_context():
        db.create_all()
    seed_database()