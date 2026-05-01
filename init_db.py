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
        "title": "Board Game Playing",
        "yearRange": "1950s–1990s",
        "category": "Strategic Systems",
        "status": "Legacy",
        "introText": "Board games played a central role in early artificial intelligence research because they provide controlled environments with fixed rules, limited actions, and clearly defined outcomes. These characteristics make them suitable for studying decision-making and reasoning. As explained by Tim French (2021), games offer a simplified domain where intelligent behaviour can be analysed without the uncertainty of real-world environments. Early AI researchers used board games as primary evidence that machines could perform structured reasoning tasks. Claude Shannon (1950) formalised computer chess as a search problem, showing that a machine could evaluate future possibilities and select optimal moves. Arthur Samuel (1959) extended this approach by incorporating learning into a checkers program, demonstrating that performance could improve through experience. These properties made board games one of the earliest and most effective forms of evidence that machines could perform structured reasoning within a well-defined domain.",
        "shortSummary": "Board game AI demonstrated how machines use search, evaluation, and optimisation to make strategic decisions in structured environments.",
        "howItWorks": "Board game AI models decision-making as a search through possible game states. A game consists of a set of possible states, a set of legal moves, a transition function defining how moves change states, and a utility function that assigns outcomes. The minimax algorithm evaluates moves by assuming both players act optimally. It explores the game tree and selects actions that maximise the AI’s outcome while minimising the opponent’s best response. In simple games such as noughts and crosses, the full game tree can be evaluated. Each possible sequence of moves is explored until a terminal state is reached, and values are propagated back through the tree to determine the optimal move. Because the number of possible states grows rapidly in more complex games, practical systems use depth-limited search, heuristic evaluation functions, and alpha-beta pruning to reduce computation.",
        "simpleExample": "In noughts and crosses, all possible outcomes can be evaluated, which guarantees optimal play when using minimax. In chess, the search space is much larger, so programs rely on evaluation functions that estimate the value of a position based on factors such as material balance and positional strength.",
        "effectiveUse": "Board game AI is used in chess engines, checkers programs, and Go systems. The same techniques are applied in planning and scheduling, optimisation problems, and strategic decision systems where search and evaluation are required.",
        "realWorldExamples": "Deep Blue demonstrated the effectiveness of large-scale search combined with domain-specific evaluation by defeating world chess champion Garry Kasparov in 1997. AlphaGo later combined search with learned evaluation functions, showing how modern systems extend classical approaches to handle complex environments such as Go.",
        "advantages": "Board game AI provides a controlled environment for testing algorithms, enables precise evaluation of decision-making strategies, and supports the development of search and optimisation techniques.",
        "limitations": "Board game AI is limited to structured environments with defined rules, does not generalise easily to complex real-world problems, and depends on accurate modelling of the domain.",
        "misuse": "Search and optimisation techniques developed for board games can be applied to high-stakes decision systems without sufficient transparency, making decisions difficult to interpret.",
        "ethics": "Success in board games may lead to overestimating AI capability. These systems operate in constrained environments and do not represent general intelligence. Distinguishing between domain-specific performance and broader intelligence remains important.",
        "waContext": "In Western Australia, board game AI is primarily used for education and training. The University of Western Australia includes game-playing algorithms such as minimax and alpha-beta pruning in its computer science curriculum. These concepts are taught through lecture material and support the development of foundational skills in adversarial search and decision-making.",
        "media": [
            {
                "id": 3,
                "type": "image",
                "url": "/static/images/minimax-diagram.png",
                "title": "Minimax Search",
                "caption": "Minimax search applied to noughts and crosses, showing how values are propagated through the game tree."
            },
            {
                "id": 30,
                "type": "image",
                "url": "/static/images/deep-blue.png",
                "title": "IBM Deep Blue",
                "caption": "Deep Blue demonstrated large-scale search and evaluation in computer chess."
            }
        ],
        "references": [
            {
                "id": 3,
                "title": "Programming a computer for playing chess",
                "url": "https://doi.org/10.1080/14786445008521796",
                "sourceType": "Research Paper",
                "accessedDate": "Accessed 2026",
                "notes": "Shannon, C. E. (1950)."
            },
            {
                "id": 31,
                "title": "Game-Playing Lecture",
                "url": "https://teaching.csse.uwa.edu.au/units/CITS3001/lectures/07GamePlaying.pdf",
                "sourceType": "Lecture Material",
                "accessedDate": "Accessed 2026",
                "notes": "French, T. (2021)."
            },
            {
                "id": 32,
                "title": "Deep Blue",
                "url": "https://www.ibm.com/history/deep-blue",
                "sourceType": "Company Source",
                "accessedDate": "Accessed 2026",
                "notes": "IBM (2011)."
            },
            {
                "id": 33,
                "title": "Mastering the game of Go",
                "url": "https://www.nature.com/articles/nature16961",
                "sourceType": "Research Paper",
                "accessedDate": "Accessed 2026",
                "notes": "Silver et al. (2016)."
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
                "url": "https://images.unsplash.com/photo-1614064641938-3bbee52942c7",
                "title": "Digital Forensics",
                "caption": "Digital forensics tools used to detect manipulated media"
            },
            {
                "id": 13,
                "type": "image",
                "url": "/static/images/deep%20fake.png",
                "title": "Synthetic Media Generation",
                "caption": "The technology behind generating synthetic media content"
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
                "url": "https://arxiv.org/abs/1406.2661",
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
                "url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600",
                "title": "Modern AI Interface",
                "caption": "The conversational interfaces that made LLMs accessible to everyone"
            },
            {
                "id": 17,
                "type": "image",    
                "url": "/static/images/large%20language%20models.png",
                "title": "LLM Architectures,Training, and Applications",
                "caption": "AI architectures, training processes, and applications of LLMs in various industries"
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