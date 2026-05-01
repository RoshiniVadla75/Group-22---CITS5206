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
        "title": "Artificial Neural Nets",
        "yearRange": "1980–2000",
        "category": "Neural Computing",
        "status": "Active",
        "introText": "Artificial Neural Nets, or Artificial Neural Networks (ANNs), are a key area of artificial intelligence inspired by the structure of the human brain. They consist of interconnected artificial neurons that learn patterns from data. ANNs became particularly important between 1980 and 2000 for tasks such as classification and pattern recognition. Early research in neural networks was criticised by researchers such as Marvin Minsky, who argued that simple neural networks without intermediate layers could not solve complex problems. This criticism contributed to a slowdown in research for a period of time. However, later developments introduced networks with multiple hidden layers, which led to the rise of deep learning. Deep learning refers to neural networks with several intermediate hidden layers, allowing systems to learn more complex patterns and relationships in data.",
        "shortSummary": "ANNs learn patterns from data through interconnected artificial neurons and later became the foundation of deep learning systems.",
        "howItWorks": "ANNs are made up of layers of neurons connected by weighted links. A typical neural network includes three main parts: an input layer, one or more hidden layers, and an output layer. Data enters through the input layer, is processed through hidden layers, and produces results in the output layer. Each neuron receives numerical inputs, applies a weighted calculation, and passes the result forward. During training, the network adjusts these weights to reduce errors and improve accuracy. In this way, the system learns patterns from data rather than following explicitly programmed rules. Deep learning extends this idea by adding multiple hidden layers. These additional layers allow the system to capture more complex relationships in the data, which improves performance in tasks such as image and speech recognition.",
        "simpleExample": "For example, an ANN can classify images of animals. The system first converts an image into numerical data, such as pixel values. These values are processed through multiple layers, where the network detects features such as edges, shapes, and colours. Based on these features, the system predicts the most likely category, such as 'cat' or 'dog'. The 'best' result is chosen based on the highest probability calculated by the network. Another example is handwriting recognition. The system learns from many examples of handwritten letters and identifies patterns in how characters are formed. When new input is given, the network compares it with learned patterns and produces the most probable output. These examples show how ANNs detect patterns and make decisions based on learned data representations.\n\nParadigm Shift: How This Changed Thinking About AI\nBefore the development of Artificial Neural Networks, computers were generally viewed as systems that followed fixed rules and produced predictable outputs. Traditional programs relied on explicitly defined instructions, and it was assumed that the same input would always produce the same result. As a result, computers were seen mainly as calculation tools rather than systems capable of adapting or improving. The introduction of neural networks challenged this assumption. Instead of relying entirely on predefined rules, ANNs could learn patterns directly from data and adjust their internal parameters through experience. This meant that a system could improve its performance over time and produce different, often better, outputs even when given similar inputs. As neural networks evolved into deep learning systems with multiple hidden layers, they demonstrated the ability to solve complex problems such as image and speech recognition. This showed that computers could go beyond simple rule-based processing and begin to mimic certain aspects of human learning. This marked a significant shift in thinking—from viewing computers as rigid, deterministic machines to recognising them as adaptive systems capable of learning from data and improving over time.",
        "effectiveUse": "Pattern recognition, image classification, speech recognition, medical diagnosis, financial prediction, and other tasks where patterns are difficult to define using explicit rules.",
        "realWorldExamples": "Facial recognition is a common real-world application of Artificial Neural Networks. The system learns patterns in facial features, such as the distances between key points on a face. These features are converted into numerical representations and compared with stored data to identify individuals. Deep learning models have significantly improved facial recognition by extracting more detailed and abstract features. The limitations of early perceptrons, such as their inability to solve the XOR problem, also encouraged the development of multi-layer networks that form the basis of modern deep learning.",
        "advantages": "ANNs can learn directly from data, model complex relationships, detect hidden patterns, and improve performance with more data.",
        "limitations": "Training neural networks can require large amounts of data and computational resources. Their internal decision-making process is often difficult to interpret, which is why they are sometimes described as 'black box' systems. Early neural networks were also limited in capability, although modern systems have overcome many of these limitations.",
        "misuse": "ANNs can be misused in surveillance using facial recognition, biased automated decision-making, and misleading prediction systems.",
        "ethics": "These uses raise ethical concerns, particularly regarding privacy, fairness, bias in training data, and lack of transparency.",
        "waContext": "Artificial Neural Networks have also played a role in the development of artificial intelligence research in Western Australia. Rather than focusing on hardware, development in WA is mainly reflected in the growth of research expertise, academic contributions, and applied projects. Research in AI and neural networks has been carried out primarily in universities and research institutions, including The University of Western Australia, Curtin University, Edith Cowan University, Murdoch University, and organisations such as CSIRO. Pawsey Supercomputing Research Centre provides advanced computational resources that support AI and neural network research, including large-scale data processing in astronomy, geoscience, and data-intensive research. Neural networks and machine learning methods are also increasingly relevant to projects such as the Square Kilometre Array, where large volumes of scientific data must be processed, filtered, and analysed.",
        "media": [
            {
                "id": 6,
                "type": "image",
                "url": "/static/images/ann-structure.png",
                "title": "Basic Structure of an Artificial Neural Network",
                "caption": "Figure 1: Basic structure of an Artificial Neural Network"
            },
            {
                "id": 7,
                "type": "image",
                "url": "/static/images/xor-problem.png",
                "title": "XOR Problem Limitation",
                "caption": "Figure 2: Limitation of early perceptrons in solving non-linearly separable problems (XOR problem)"
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
        "introText": "Natural Language Processing (NLP) is a field of artificial intelligence that enables computers to read, “understand”, and generate human language. Here, “understand” refers to the ability of systems to process and analyse language patterns, rather than true human-like comprehension. It has developed alongside advances in computing power and data. Early NLP systems were rule-based, relying on predefined linguistic rules. In contrast, modern NLP mainly uses machine learning and deep learning techniques. Transformer-based models are now the dominant approach, as they can handle a wide range of language tasks effectively. These models have significantly improved the ability of systems to process and generate human-like language.",
        "shortSummary": "NLP enables computers to process and generate human language using tokenisation, vector representations, and transformer-based models.",
        "howItWorks": "NLP systems convert human language into numerical representations so that computers can process it. A key step is tokenisation, which splits text into smaller units such as words or subwords. These tokens are then converted into vectors, which are numerical representations of words. Vectors allow the system to capture relationships between words, such as similarity in meaning. Modern NLP systems, especially transformer models, use attention mechanisms to understand context by focusing on important words in a sentence and considering how words relate to each other. Overall, NLP follows a general process: input text is tokenised, converted into vectors, processed by a model, and then transformed into an output such as a response or prediction. It is important to note that NLP systems do not truly 'understand' language in the same way humans do. Instead, they identify patterns in text, such as nouns, verbs, and sentence structure, and assign meaning based on statistical relationships learned from data.",
        "simpleExample": "For example, consider the input: 'book a flight to Sydney tomorrow'. The system first splits the sentence into tokens and converts them into vectors. It then analyses these vectors to identify patterns that suggest the user’s intent, such as booking a flight, and extracts key information like destination and time. Based on this, the system generates an appropriate response or action. Another example is a search query such as 'best cafe near me open now'. The system processes the words as tokens, converts them into vectors, and uses learned patterns to understand the meaning of the query. It then considers factors such as location, time, and user intent to provide relevant results. These examples show how NLP systems process language step by step and make decisions based on learned patterns rather than explicit rules.\n\nParadigm Shift: How This Changed Thinking About AI\nBefore the development of Natural Language Processing, computers were generally seen as systems that could only handle structured, numerical data. Human language was considered too complex, ambiguous, and context-dependent for machines to process effectively. As a result, interaction with computers was limited to formal commands and predefined inputs. The introduction of NLP challenged this view by enabling computers to process and generate human language. Early rule-based systems showed that language could be analysed using structured rules, but their limitations highlighted the complexity of real-world communication. Later, the shift to machine learning and deep learning approaches allowed systems to learn language patterns directly from large datasets rather than relying entirely on predefined rules. With the development of transformer-based models, NLP systems became capable of handling a wide range of tasks, such as translation, question answering, and text generation. These systems could produce outputs that appear meaningful and context-aware, even though they do not truly 'understand' language in a human sense. This marked a significant shift in thinking—from viewing computers as tools limited to structured data processing to recognising them as systems that can interact with human language in flexible and increasingly natural ways.",
        "effectiveUse": "Speech recognition, machine translation, sentiment analysis, chatbots, dialogue systems, summarisation, question answering, and information extraction.",
        "realWorldExamples": "Transformer models are widely used in industry. Libraries such as Hugging Face Transformers support tasks including translation and text classification. Models such as BERT and GPT can perform multiple language tasks using the same architecture. These models generate outputs based on learned statistical patterns rather than true understanding of language, and they are commonly applied in chatbots, search engines, and customer support systems.",
        "advantages": "NLP systems can process large amounts of text quickly, operate continuously without fatigue, and automate repetitive language tasks. Transformer models are flexible and can be adapted to different applications.",
        "limitations": "Human language is complex and highly context-dependent, which makes full understanding difficult. NLP models rely heavily on training data, which can introduce bias. They learn statistical patterns rather than true understanding, which may lead to incorrect or misleading outputs. Transformer models also require significant computational resources, making them expensive to train and deploy.",
        "misuse": "NLP technologies can be misused to generate fake or misleading content, automate scams or spam messages, and produce biased or harmful text.",
        "ethics": "These issues can affect public trust and raise ethical concerns about bias, misinformation, harmful outputs, and the responsible use of AI systems.",
        "waContext": "Natural Language Processing has also contributed to the development of artificial intelligence research in Western Australia. Similar to other AI fields, the focus in WA is mainly on the growth of research expertise, academic contributions, and applied projects rather than specific hardware developments. NLP-related research has been carried out primarily within universities and research institutions, including The University of Western Australia, Curtin University, Edith Cowan University, Murdoch University, and organisations such as CSIRO. The development of NLP in WA reflects a broader evolution from early rule-based systems to modern machine learning and deep learning approaches. Recent developments have been supported by advanced research infrastructure such as the Pawsey Supercomputing Research Centre, which provides computational power for large-scale NLP models and scientific research. NLP techniques are also increasingly relevant in large-scale projects such as the Square Kilometre Array, where textual and metadata information must be processed, organised, and analysed.",
        "media": [
            {
                "id": 14,
                "type": "image",
                "url": "/static/images/nlp-pipeline.png",
                "title": "NLP Processing Pipeline",
                "caption": "Figure 1: Basic pipeline of a Natural Language Processing system"
            },
            {
                "id": 15,
                "type": "image",
                "url": "/static/images/pawsey-centre.png",
                "title": "Pawsey Supercomputing Research Centre",
                "caption": "Figure 2: Pawsey Supercomputing Research Centre, supporting AI and NLP research in Western Australia"
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
                "title": "Transformers: State-of-the-art natural language processing",
                "url": "https://aclanthology.org/2020.emnlp-demos.6.pdf",
                "sourceType": "Conference Paper",
                "accessedDate": "2026",
                "notes": "Wolf et al. (2020)"
            },
            {
                "id": 16,
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