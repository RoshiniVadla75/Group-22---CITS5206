const topics = [
  {
    id: 1,
    slug: "turing-thoughts-on-ai",
    title: "Alan Turing's Thoughts on AI",
    yearRange: "c. 1950",
    category: "Foundations",
    introText: "Alan Turing's ideas laid the intellectual groundwork for artificial intelligence. His questions about whether machines can think became central to later AI research.",
    shortSummary: "Turing provided the conceptual foundations for machine intelligence.",
    howItWorks: "This topic focuses on theoretical ideas about computation, intelligence, and symbolic reasoning rather than a single application system.",
    simpleExample: "A machine following formal logical steps to solve a problem reflects Turing's vision of computation.",
    effectiveUse: "Most effective in foundational teaching, philosophy of AI, and computational theory.",
    realWorldExamples: "University teaching, theoretical computer science, and early AI research.",
    advantages: "Provides a strong conceptual basis for later technologies.",
    limitations: "Highly theoretical and not a direct end-user system.",
    misuse: "Can be oversimplified when discussing modern AI.",
    ethics: "Raises questions about intelligence, autonomy, and human-machine comparison.",
    waContext: "The University of Western Australia's Computer Science department has long incorporated Turing's theories into its foundational curriculum.",
    media: [
      {
        id: 1,
        type: "image",
        url: "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1200&q=80",
        title: "Computing Foundations",
        caption: "Theoretical work shaped the future of AI."
      }
    ],
    references: [
      {
        id: 1,
        title: "Foundational AI History",
        url: "https://en.wikipedia.org/wiki/Alan_Turing",
        sourceType: "Background Source",
        accessedDate: "Accessed 2026",
        notes: "General background on Turing and computing history."
      }
    ]
  },
  {
    id: 2,
    slug: "learning-machines",
    title: "Learning Machines",
    yearRange: "c. 1960",
    category: "Machine Learning",
    introText: "Learning machines marked a shift from explicit programming toward systems that could improve through data and experience.",
    shortSummary: "Machines began to learn patterns rather than rely only on fixed hand-written rules.",
    howItWorks: "These systems use training data to identify patterns and improve decision-making over time.",
    simpleExample: "A model trained on past weather data predicts tomorrow's temperature range.",
    effectiveUse: "Useful when large amounts of data are available and patterns can be learned statistically.",
    realWorldExamples: "Prediction systems, classification, industrial monitoring, and analytics.",
    advantages: "Can adapt better than rigid rule-based systems in changing environments.",
    limitations: "Needs data quality, computational power, and careful evaluation.",
    misuse: "Can produce misleading results when trained on biased or poor-quality data.",
    ethics: "Raises concerns about fairness, transparency, and accountability.",
    waContext: "WA universities and research groups have contributed to machine learning education and research.",
    media: [
      {
        id: 1,
        type: "image",
        url: "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=1200&q=80",
        title: "Learning from Data",
        caption: "Data-driven approaches transformed AI development."
      }
    ],
    references: [
      {
        id: 1,
        title: "Machine Learning Overview",
        url: "https://en.wikipedia.org/wiki/Machine_learning",
        sourceType: "Background Source",
        accessedDate: "Accessed 2026",
        notes: "General introductory material."
      }
    ]
  },
  {
    id: 3,
    slug: "game-playing-ai",
    title: "Game Playing AI",
    yearRange: "c. 1970",
    category: "Strategic Systems",
    introText: "Game-playing AI demonstrated that machines could make strategic decisions in structured environments.",
    shortSummary: "Game AI made abstract reasoning and search visible and measurable.",
    howItWorks: "These systems explore possible future moves and evaluate game states to choose effective strategies.",
    simpleExample: "A chess engine examines several possible moves and chooses the one with the highest evaluation.",
    effectiveUse: "Best in structured problems with clear rules and goals.",
    realWorldExamples: "Chess engines, board games, and teaching search algorithms.",
    advantages: "Excellent for demonstrating planning and search methods.",
    limitations: "Performs best in closed systems with well-defined rules.",
    misuse: "People may assume success in games always transfers to messy real-world tasks.",
    ethics: "Limited direct ethical risk, but influences public perception of AI capability.",
    waContext: "WA computing programs have used game-playing systems as teaching tools for search, heuristics, and decision-making.",
    media: [
      {
        id: 1,
        type: "image",
        url: "https://images.unsplash.com/photo-1528819622765-d6bcf132f793?auto=format&fit=crop&w=1200&q=80",
        title: "Strategic Search",
        caption: "Game environments provided clear testbeds for AI reasoning."
      }
    ],
    references: [
      {
        id: 1,
        title: "Game AI Background",
        url: "https://en.wikipedia.org/wiki/Game_artificial_intelligence",
        sourceType: "Background Source",
        accessedDate: "Accessed 2026",
        notes: "General overview source."
      }
    ]
  },
  {
    id: 4,
    slug: "expert-systems",
    title: "Expert Systems",
    yearRange: "c. 1980",
    category: "Knowledge Engineering",
    introText: "In the 1980s, expert systems became the first commercially successful form of AI. These programs encoded the decision-making knowledge of human experts into software using rules, facts, and inference engines. Systems like MYCIN, DENDRAL, and R1/XCON demonstrated that AI could provide practical value in professional domains.",
    shortSummary: "Expert systems captured human specialist knowledge in rule-based software, enabling computers to make decisions in medicine, finance, and engineering by following chains of if-then logic.",
    howItWorks: "An expert system consists of three components: a knowledge base, an inference engine, and a user interface. The knowledge base stores rules and facts collected from experts. The inference engine applies these rules step by step to reach a conclusion.",
    simpleExample: "If a patient has fever and cough, and recently travelled, the system may suggest considering a tropical disease. This imitates how a specialist reasons from symptoms to diagnosis.",
    effectiveUse: "Most effective in narrow domains where knowledge can be clearly expressed as rules, such as diagnosis, equipment configuration, tax advice, and troubleshooting.",
    realWorldExamples: "MYCIN for medical diagnosis, DENDRAL for chemistry, and XCON for configuring computer systems at Digital Equipment Corporation.",
    advantages: "They preserve expert knowledge, provide consistent decisions, and work well in specialised areas where human expertise is expensive or scarce.",
    limitations: "They are brittle, hard to maintain, and struggle with uncertainty, ambiguity, and rapidly changing domains. Building the knowledge base is also labour-intensive.",
    misuse: "They can be misused when applied outside their narrow domain, or when users trust them too much without human verification.",
    ethics: "Important concerns include accountability for wrong recommendations, transparency of rules, and over-reliance on automated advice in high-stakes domains.",
    waContext: "Expert systems influenced decision support work in WA across mining, agriculture, and environmental management, where codified knowledge could be embedded into software tools.",
    media: [
      {
        id: 1,
        type: "image",
        url: "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=1200&q=80",
        title: "Knowledge Engineering Process",
        caption: "The process of capturing expert knowledge into rule-based systems."
      },
      {
        id: 2,
        type: "image",
        url: "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=1200&q=80",
        title: "Medical Expert Systems",
        caption: "Expert systems found early success in medical diagnosis."
      }
    ],
    references: [
      {
        id: 1,
        title: "Rule-based Expert Systems",
        url: "https://en.wikipedia.org/wiki/Expert_system",
        sourceType: "Background Source",
        accessedDate: "Accessed 2026",
        notes: "General overview of expert systems."
      }
    ]
  },
    {
    id: 5,
    slug: "artificial-neural-nets",
    title: "Artificial Neural Networks",
    yearRange: "1980–2000",
    category: "Neural Computing",
    introText: "Artificial neural networks (ANNs) experienced a renaissance in the 1980s with the development of backpropagation — an efficient algorithm for training multi-layer networks. Unlike expert systems, neural networks could learn patterns directly from data without explicit rules, making them suited for tasks like image recognition, speech processing, and financial prediction.",
    shortSummary: "Inspired by the human brain, artificial neural networks learned complex patterns through layers of interconnected nodes, overcoming the limitations of earlier approaches and laying the foundation for deep learning.",
    howItWorks: "A neural network consists of layers of artificial neurons (nodes). Each connection between nodes has a weight. Data enters the input layer, passes through hidden layers where weighted sums are computed and activation functions applied, and produces output. During training, backpropagation calculates how much each weight contributed to errors, then adjusts weights to reduce future errors. Through thousands of iterations, the network learns to map inputs to correct outputs.",
    simpleExample: "Imagine a team passing a message through a chain. Each person slightly modifies the message based on what they think is important. After checking if the final message is correct, feedback goes back through the chain — each person adjusts how they modify messages. After many rounds, the team reliably produces correct messages.",
    effectiveUse: "Pattern recognition in images, speech, and text. Regression and classification tasks. Applications where the underlying rules are too complex to express explicitly but sufficient training data exists.",
    realWorldExamples: "Handwriting recognition (used in postal sorting), early speech recognition systems, financial market prediction models, and medical image analysis. LeCun's convolutional neural networks for digit recognition at Bell Labs became a landmark achievement.",
    advantages: "Could learn complex, non-linear patterns that rule-based systems couldn't capture. Generalised to new, unseen data. Required no manual knowledge engineering — learning was automatic. Scaled with more data and computation.",
    limitations: "Required large amounts of training data. Training was computationally expensive with 1980s-2000s hardware. Networks were 'black boxes' — difficult to explain why a particular decision was made. Prone to overfitting on small datasets.",
    misuse: "Black-box nature allowed deployment in high-stakes decisions (credit scoring, criminal justice) without explainability. Biased training data produced biased models that could discriminate against protected groups without anyone understanding why.",
    ethics: "The opacity of neural network decisions raises accountability concerns. When a neural network denies someone a loan or flags them as suspicious, the lack of explainable reasoning conflicts with requirements for fair, transparent decision-making.",
    waContext: "WA universities, particularly UWA and Curtin, established neural computing research groups in the 1990s. Applications in mineral exploration, environmental monitoring, and agricultural prediction were developed by WA researchers, applying neural networks to the state's dominant industries.",
    media: [
      {
        id: 9,
        type: "image",
        title: "Neural Network Architecture",
        url: "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600",
        caption: "Visualisation of neural network layers and connections"
      },
      {
        id: 10,
        type: "image",
        title: "Brain-Inspired Computing",
        url: "https://images.unsplash.com/photo-1559757175-5700dde675bc?w=600",
        caption: "Neural networks drew inspiration from biological neural structures"
      }
    ],
    references: [
      {
        id: 9,
        title: "Learning Representations by Back-propagating Errors",
        url: "https://www.nature.com/articles/323533a0",
        sourceType: "Research Paper",
        accessedDate: "2024-02-15",
        notes: "Rumelhart, Hinton & Williams' seminal 1986 paper"
      },
      {
        id: 10,
        title: "Neural Networks and Deep Learning",
        url: "http://neuralnetworksanddeeplearning.com/",
        sourceType: "Online Book",
        accessedDate: "2024-02-15",
        notes: "Michael Nielsen's accessible introduction"
      }
    ]
  },
  {
    id: 6,
    slug: "internet-driven-ai-ibm-watson",
    title: "Internet-Driven AI / IBM Watson",
    yearRange: "c. 2011",
    category: "Knowledge Retrieval",
    introText: "In 2011, IBM Watson competed on Jeopardy! against champions Ken Jennings and Brad Rutter — and won. Watson represented a new paradigm: AI that could process enormous volumes of unstructured text, understand natural language questions, and generate accurate answers in real time. The internet age had created vast repositories of human knowledge, and Watson showed that AI could harness this information at superhuman speed.",
    shortSummary: "IBM Watson demonstrated that AI could process vast amounts of internet-scale data to answer natural language questions, defeating Jeopardy! champions and showcasing a new era of knowledge-driven AI.",
    howItWorks: "Watson used a massively parallel architecture called DeepQA. When given a question, it generated hundreds of candidate answers by searching through millions of documents. It then used over 100 different scoring algorithms to evaluate each candidate — checking evidence from multiple sources, analysing linguistic patterns, and assessing confidence. The candidate with the highest aggregate confidence score was selected as the answer. All of this happened in under 3 seconds.",
    simpleExample: "Imagine asking a question and having a thousand researchers simultaneously search through every encyclopedia, textbook, and article ever written, each providing their best answer with a confidence level. Watson essentially does this digitally, then picks the answer that the most 'researchers' agree on.",
    effectiveUse: "Question answering, information retrieval, medical literature analysis, legal document review, customer service automation, and any domain requiring synthesis of large text corpora.",
    realWorldExamples: "Watson for Oncology assisted doctors by analysing medical literature for treatment recommendations. Watson Discovery helped legal firms search case law. Watson Assistant powers enterprise customer service chatbots. The Jeopardy! victory remains its most famous demonstration.",
    advantages: "Could process and synthesise information from millions of documents. Provided evidence-based answers with confidence scores. Worked with unstructured natural language rather than requiring structured queries. Demonstrated practical AI value to a mass audience.",
    limitations: "Required enormous computational resources. Watson for Oncology faced criticism for providing unsafe treatment recommendations in some cases. The system struggled with domains where evidence was ambiguous or rapidly changing. Commercialisation proved more difficult than the dramatic demo suggested.",
    misuse: "IBM's marketing overpromised Watson's capabilities, leading to failed implementations in healthcare and other domains. The gap between demonstration performance and real-world deployment highlighted risks of AI hype.",
    ethics: "Raised concerns about AI in medical decision-making — who is accountable when Watson recommends an incorrect treatment? Also highlighted the danger of treating AI as infallible authority because of impressive demonstrations.",
    waContext: "WA's healthcare and resources sectors explored Watson-style AI for document analysis and decision support. Perth hospitals investigated AI-assisted diagnosis tools influenced by Watson's approach. WA's tech sector began positioning itself in the enterprise AI space following Watson's high-profile success.",
    media: [
      {
        id: 11,
        type: "image",
        title: "Watson on Jeopardy!",
        url: "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=600",
        caption: "AI competing against human champions in knowledge retrieval"
      },
      {
        id: 12,
        type: "image",
        title: "Big Data Processing",
        url: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600",
        caption: "The massive data processing infrastructure behind Watson"
      }
    ],
    references: [
      {
        id: 11,
        title: "Building Watson: An Overview of the DeepQA Project",
        url: "https://www.aaai.org/ojs/index.php/aimagazine/article/view/2303",
        sourceType: "Research Paper",
        accessedDate: "2024-02-20",
        notes: "IBM Research's technical overview of Watson's architecture"
      },
      {
        id: 12,
        title: "Watson: Beyond Jeopardy!",
        url: "https://www.ibm.com/watson",
        sourceType: "Web Archive",
        accessedDate: "2024-02-20",
        notes: "IBM's Watson platform documentation"
      }
    ]
  },
  {
    id: 7,
    slug: "evolutionary-computing-genetic-algorithms",
    title: "Evolutionary Computing & Genetic Algorithms",
    yearRange: "c. 2010",
    category: "Bio-Inspired AI",
    introText: "Evolutionary computing draws direct inspiration from biological evolution. Genetic algorithms (GAs) create populations of candidate solutions, evaluate their fitness, and breed the best performers through crossover and mutation. Over many generations, solutions evolve to optimise complex problems that traditional methods struggle with. By the 2010s, evolutionary approaches were applied to engineering design, logistics, scheduling, and even creative applications.",
    shortSummary: "Genetic algorithms applied Darwin's principles of natural selection to computing — evolving solutions to complex problems through mutation, crossover, and survival of the fittest.",
    howItWorks: "A genetic algorithm starts with a random population of solutions, each encoded as a 'chromosome' (string of parameters). A fitness function evaluates each solution's quality. The best performers are selected as 'parents' and combined through crossover (mixing parts of two solutions) and mutation (randomly changing elements). This produces a new generation. The process repeats for hundreds or thousands of generations, with solutions progressively improving through simulated natural selection.",
    simpleExample: "Imagine designing the perfect paper airplane. You create 100 random designs, throw them all, and measure distance. Take the 10 best, combine features from pairs of top performers (fold style from one, wing shape from another), add small random changes, and create 100 new designs. Repeat 1000 times. The final designs will fly remarkably well.",
    effectiveUse: "Optimisation problems with large search spaces where exact solutions are impractical: engineering design, scheduling, routing, parameter tuning, circuit design, and creative applications like evolving art or music.",
    realWorldExamples: "NASA used genetic algorithms to design antenna shapes for spacecraft. Automotive companies evolved crash-resistant vehicle structures. Logistics companies optimised delivery routes. Financial firms evolved trading strategies. Even artistic applications emerged — evolving visual art and music compositions.",
    advantages: "Can find good solutions to problems too complex for analytical approaches. Don't require gradient information or continuous functions. Can explore multiple solution areas simultaneously. Naturally avoid getting stuck in local optima. Produce creative, unexpected solutions that human designers might not consider.",
    limitations: "No guarantee of finding the global optimum. Computationally expensive for large populations over many generations. Fitness function design is critical and can bias results. Parameter tuning (population size, mutation rate, crossover method) requires expertise.",
    misuse: "Genetic algorithms have been used to evolve adversarial attacks on other AI systems. Automated optimisation without constraints can produce technically efficient but ethically problematic solutions.",
    ethics: "When evolutionary algorithms optimise for narrow fitness criteria, they can discover solutions that exploit loopholes or cause unintended consequences. This highlights the importance of defining optimisation goals carefully and considering broader impacts.",
    waContext: "WA researchers have applied genetic algorithms extensively in mining optimisation — from pit design to ore processing schedules. UWA and Curtin have active research groups in evolutionary computing. The WA resources sector's complex logistics and scheduling problems make it a natural application domain for evolutionary approaches.",
    media: [
      {
        id: 13,
        type: "image",
        title: "Evolutionary Process Diagram",
        url: "https://images.unsplash.com/photo-1530026405186-ed1f139313f8?w=600",
        caption: "The cycle of selection, crossover, and mutation in genetic algorithms"
      },
      {
        id: 14,
        type: "image",
        title: "Optimisation in Nature",
        url: "https://images.unsplash.com/photo-1500462918059-b1a0cb512f1d?w=600",
        caption: "Nature's evolutionary processes inspire computational optimisation"
      }
    ],
    references: [
      {
        id: 13,
        title: "Genetic Algorithms in Search, Optimization and Machine Learning",
        url: "https://dl.acm.org/doi/book/10.5555/534133",
        sourceType: "Book",
        accessedDate: "2024-03-01",
        notes: "Goldberg's foundational textbook on genetic algorithms"
      },
      {
        id: 14,
        title: "Evolutionary Computation: Toward a New Philosophy of Machine Intelligence",
        url: "https://ieeexplore.ieee.org/",
        sourceType: "Book",
        accessedDate: "2024-03-01",
        notes: "Fogel's comprehensive overview of the field"
      }
    ]
  },
  {
    id: 8,
    slug: "Synthetic Media Technology-deep-fakes",
    title: "Synthetic Media Technology / Deep Fakes",
    yearRange: "c. 2015",
    category: "Generative AI & Deception",
    introText: "Deep fakes emerged around 2015 as advances in deep learning — particularly Generative Adversarial Networks (GANs) — made it possible to create highly realistic fake media. A 'deep fake' uses neural networks to swap faces in video, clone voices, or generate entirely synthetic images of people who don't exist. The technology rapidly improved from obvious fakes to nearly undetectable fabrications, creating urgent challenges for journalism, democracy, and personal security.",
    shortSummary: "Deep fake technology uses neural networks to create convincing fake images, audio, and video, raising unprecedented challenges for trust, media integrity, and digital security.",
    howItWorks: "Most deep fakes use Generative Adversarial Networks (GANs), which pit two neural networks against each other: a Generator creates fake content, and a Discriminator tries to identify fakes. They train together in competition — the Generator improves at creating realistic fakes while the Discriminator improves at detecting them. Through thousands of training rounds, the Generator produces increasingly convincing content. Face-swapping specifically uses autoencoders that learn to reconstruct faces, then swap the encoding of one face onto another's structure.",
    simpleExample: "Imagine two art students: one creates forgeries of famous paintings, the other tries to spot them. They keep competing — the forger gets better at copying, the detective gets better at spotting fakes. Eventually, the forgeries become nearly indistinguishable from originals.",
    effectiveUse: "Film and entertainment (de-aging actors, visual effects), accessibility (translating sign language, dubbing content), art and creative expression, privacy protection (anonymising faces in footage), and medical imaging augmentation for training purposes.",
    realWorldExamples: "Face-swapping in Hollywood films (de-aging Robert De Niro in The Irishman). Voice cloning for accessibility applications. Synthetic media for training datasets. Unfortunately also used to create non-consensual intimate imagery and political disinformation.",
    advantages: "Enables powerful creative and entertainment applications. Can protect privacy by generating synthetic stand-ins. Aids in medical research through synthetic data generation. Demonstrates remarkable advances in generative AI capability.",
    limitations: "Current detection tools are in an arms race with generation tools. Subtle artifacts (blinking patterns, skin texture, lighting inconsistencies) can reveal fakes but detection is not reliable. Once shared, fake content spreads faster than debunking.",
    misuse: "Non-consensual intimate imagery (the most common misuse), political disinformation, financial fraud through voice cloning, identity theft, fabricated evidence, and erosion of trust in all digital media.",
    ethics: "Deep fakes represent one of the most urgent ethical challenges in AI. They threaten informed consent, democratic processes, journalism integrity, and personal safety. The technology forces society to reconsider what constitutes 'evidence' and 'truth' in the digital age.",
    waContext: "WA law enforcement and cybersecurity researchers have been active in deep fake detection research. Edith Cowan University's Security Research Institute has studied digital forensics approaches to identifying manipulated media. WA's growing cybersecurity sector positions the state as a contributor to the global response to synthetic media threats.",
    media: [
      {
        id: 15,
        type: "image",
        title: "Synthetic Media Generation",
        url: "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600",
        caption: "The technology behind generating synthetic media content"
      },
      {
        id: 16,
        type: "image",
        title: "Digital Forensics",
        url: "https://images.unsplash.com/photo-1563986768609-322da13575f2?w=600",
        caption: "Digital forensics tools used to detect manipulated media"
      }
    ],
    references: [
      {
        id: 15,
        title: "Generative Adversarial Networks",
        url: "https://arxiv.org/abs/1406.2661",
        sourceType: "Research Paper",
        accessedDate: "2024-03-10",
        notes: "Goodfellow et al.'s original GAN paper"
      },
      {
        id: 16,
        title: "The State of Deepfakes",
        url: "https://regmedia.co.uk/2019/10/08/deepfake_report.pdf",
        sourceType: "Report",
        accessedDate: "2024-03-10",
        notes: "Deeptrace's comprehensive analysis of deep fake proliferation"
      }
    ]
  },
  {
    id: 9,
    slug: "natural-language-processing",
    title: "Natural Language Processing",
    yearRange: "2010–2020",
    category: "Language AI",
    introText: "Natural Language Processing (NLP) advanced dramatically between 2010 and 2020, driven by deep learning breakthroughs. The introduction of word embeddings (Word2Vec, 2013), attention mechanisms, and the Transformer architecture (2017) revolutionised how machines process language. These advances enabled machine translation that approached human quality, sentiment analysis at scale, and question-answering systems that could understand context and nuance.",
    shortSummary: "NLP transformed how computers understand, interpret, and generate human language, enabling machine translation, sentiment analysis, and the precursors to modern AI assistants.",
    howItWorks: "Modern NLP converts words into numerical vectors (embeddings) that capture semantic relationships — 'king' minus 'man' plus 'woman' approximately equals 'queen.' The Transformer architecture introduced self-attention, allowing models to weigh the importance of different words in context. Instead of processing text sequentially, Transformers examine all words simultaneously, learning which words relate to each other regardless of distance in the text. This parallel processing enabled training on much larger datasets.",
    simpleExample: "Imagine reading a sentence and highlighting which words help you understand each other word. In 'The cat sat on the mat because it was tired,' you'd connect 'it' to 'cat' (not 'mat'). A Transformer does this automatically for every word pair, building a web of relationships.",
    effectiveUse: "Machine translation, sentiment analysis, named entity recognition, text summarisation, question answering, chatbots, search engine improvement, and content recommendation systems.",
    realWorldExamples: "Google Translate's dramatic quality improvement (2016 onwards using neural machine translation). Virtual assistants (Siri, Alexa, Google Assistant). Automated email replies (Gmail's Smart Reply). Sentiment analysis tools used by businesses to monitor customer feedback.",
    advantages: "Broke the language barrier in computing — machines could finally work with human language at useful quality. Enabled automation of previously labour-intensive text processing tasks. Scaled to process billions of documents. Cross-lingual capabilities improved international communication.",
    limitations: "Models struggled with sarcasm, irony, and cultural context. Required enormous training datasets that reflected existing biases. Smaller and endangered languages were underserved. Processing long documents remained challenging until very recent advances.",
    misuse: "Automated content generation for spam and disinformation. Mass surveillance through text analysis. Manipulation through sentiment-aware targeted messaging. Automated censorship systems.",
    ethics: "NLP systems trained on internet text inevitably absorb societal biases — gender, racial, cultural. These biases get amplified when systems operate at scale. The digital divide means NLP advances primarily benefit major languages, potentially marginalising linguistic diversity.",
    waContext: "WA researchers have applied NLP to mining industry document analysis, environmental impact assessments, and Indigenous language preservation projects. The University of Western Australia has contributed to NLP research in specialised domains relevant to WA's key industries.",
    media: [
      {
        id: 17,
        type: "image",
        title: "Language Processing Pipeline",
        url: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600",
        caption: "The complex pipeline of processing natural language"
      },
      {
        id: 18,
        type: "image",
        title: "Transformer Architecture",
        url: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600",
        caption: "The Transformer architecture revolutionised NLP"
      }
    ],
    references: [
      {
        id: 17,
        title: "Attention Is All You Need",
        url: "https://arxiv.org/abs/1706.03762",
        sourceType: "Research Paper",
        accessedDate: "2024-03-15",
        notes: "The foundational Transformer paper by Vaswani et al."
      },
      {
        id: 18,
        title: "Efficient Estimation of Word Representations in Vector Space",
        url: "https://arxiv.org/abs/1301.3781",
        sourceType: "Research Paper",
        accessedDate: "2024-03-15",
        notes: "Mikolov et al.'s Word2Vec paper"
      }
    ]
  },
  {
    id: 10,
    slug: "large-language-models",
    title: "Large Language Models",
    yearRange: "2024",
    category: "Frontier AI",
    introText: "Large Language Models (LLMs) are the culmination of decades of AI research, scaling Transformer architectures to hundreds of billions of parameters trained on vast text corpora. Beginning with GPT-3 (2020) and rapidly advancing through GPT-4, Claude, Gemini, and LLaMA, these models demonstrate emergent capabilities that surprise even their creators — from writing code and poetry to passing professional exams and engaging in nuanced reasoning.",
    shortSummary: "Large language models like GPT-4, Claude, and Gemini represent the current frontier of AI — systems that can generate text, reason, code, and converse with unprecedented fluency and capability.",
    howItWorks: "LLMs are Transformer neural networks trained on trillions of words from the internet, books, and other text sources. During training, the model learns to predict the next word in a sequence, developing internal representations of grammar, facts, reasoning patterns, and even some form of world knowledge. At inference time, the model generates text word by word, with each word choice influenced by all previous context. Techniques like Reinforcement Learning from Human Feedback (RLHF) further refine the model's outputs to be helpful, honest, and harmless.",
    simpleExample: "Imagine someone who has read every book, article, and website ever written, and has an extraordinary memory for patterns and relationships. When you ask them a question, they generate an answer by predicting, word by word, what the most helpful and accurate response would look like based on everything they've read.",
    effectiveUse: "Writing assistance, code generation, analysis and summarisation, education and tutoring, creative brainstorming, customer service, research assistance, language translation, and as reasoning components in larger AI systems.",
    realWorldExamples: "ChatGPT reached 100 million users within two months of launch. GitHub Copilot assists millions of developers. Claude helps with research and analysis. Google's Gemini integrates AI into search. LLMs now power applications across every industry from healthcare to law to education.",
    advantages: "Unprecedented versatility — one model handles thousands of tasks. Natural language interface makes AI accessible to non-technical users. Can reason, plan, and generate creative content. Rapidly improving capabilities with each generation. Democratising access to sophisticated AI assistance.",
    limitations: "Hallucinations — confidently generating false information. Enormous computational and energy costs. Training data cutoff means limited current knowledge. Difficulty with precise calculation and formal logic. Potential for generating harmful content despite safety measures.",
    misuse: "Mass generation of disinformation. Automated social engineering and phishing. Academic dishonesty. Creation of malicious code. Overwhelming human content creators and journalists. Impersonation and fraud at unprecedented scale.",
    ethics: "LLMs raise profound questions about intellectual property (trained on copyrighted works), employment displacement, educational integrity, information reliability, and the concentration of AI power in a few large companies. The energy consumption of training and running these models also raises environmental concerns.",
    waContext: "WA's technology sector is rapidly adopting LLMs across mining, agriculture, healthcare, and education. Perth-based startups are building LLM-powered tools for the resources industry. WA universities are integrating AI literacy into curricula and researching LLM applications for remote and regional service delivery — a key concern for geographically vast Western Australia.",
    media: [
      {
        id: 19,
        type: "image",
        title: "Modern AI Interface",
        url: "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600",
        caption: "The conversational interfaces that made LLMs accessible to everyone"
      },
      {
        id: 20,
        type: "image",
        title: "AI Computing Infrastructure",
        url: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600",
        caption: "The massive computing infrastructure required to train LLMs"
      }
    ],
    references: [
      {
        id: 19,
        title: "GPT-4 Technical Report",
        url: "https://arxiv.org/abs/2303.08774",
        sourceType: "Research Paper",
        accessedDate: "2024-03-20",
        notes: "OpenAI's technical report on GPT-4"
      },
      {
        id: 20,
        title: "On the Dangers of Stochastic Parrots",
        url: "https://dl.acm.org/doi/10.1145/3442188.3445922",
        sourceType: "Research Paper",
        accessedDate: "2024-03-20",
        notes: "Bender et al.'s influential critique of LLMs"
      }
    ]
  }
];
function getTopicBySlug(slug) {
  return topics.find(topic => topic.slug === slug);
}

function getAdjacentTopics(id) {
  const index = topics.findIndex(topic => topic.id === id);
  return {
    prev: index > 0 ? topics[index - 1] : null,
    next: index < topics.length - 1 ? topics[index + 1] : null
  };
}