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
        "shortSummary": "Large Language Models (LLMs) like GPT-4, Claude, Gemini, and Llama represent the cutting edge of AI in 2024. Trained on trillions of words and hundreds of billions of parameters, they exhibit capabilities by performing tasks they were never explicitly trained for and are transforming every industry.",
        "howItWorks": "LLMs are extremely large transformer neural networks trained on vast internet text using self-supervised learning (predicting the next word). Their scale creates emergent capabilities: reasoning, code generation, instruction following, translation, mathematics, and creative writing - all from the same model. Reinforcement learning from Human Feedback (RLHF) is used to align model outputs with human preferences and safety guidelines. Models are accessed via Application Programming Interfaces (APIs) or run locally on consumer hardware.",
        "simpleExample": "Ask an LLM: ‘Explain quantum entanglement to a 10-year-old using a story about socks.’ The model has never seen that exact prompt but draws on its training to craft an age-appropriate metaphor, with narrative structure and accurate physics - an example of generalisation for beyond simple pattern matching.",
        "effectiveUse": "LLMs are most effective as flexible general-purpose assistants for text generation, code writing, summarisation, Q&A, translation, tutoring, creative writing, and data analysis. They are transforming software development, education, legal research, scientific writing, and customer service",
        "realWorldExamples": "ChatGPT (OpenAI) reached 100 million users in two months – the fastest growing consumer application in history. GitHub Copilot, powered by OpenAI, assists millions of developers with code. Claude (Anthropic) is used for long-form document analysis. Google Gemini integrates into Google Workspace. Meta’s Llama models enable open-source deployment on consumer hardware.",
        "advantages over human intelligence": "LLMs can process and generate text at a speed and scale that humans cannot match. They can draft multiple versions of a response quickly, work across many subject areas, and handle large volumes of text without fatigue. In educational settings, they can provide immediate feedback and different levels of explanation, which can be useful when supervised carefully.",
        "limitations": "LLMs do not truly understand meaning in the human sense. They can hallucinate - generating confident, fluent, but factually wrong information. They have knowledge cutoffs and cannot access real-time information without tools. They can be inconsistent across sessions. Very large models require enormous compute resources. Fine-tuned alignment is imperfect; models can still harmful outputs. ",
        "misuse": "Because they produce persuasive text quickly, LLMs can be misused for disinformation, phishing messages, spam, academic misconduct, or the generation of misleading summaries that appear confident but are wrong. Their ease of use lowers the barrier for harmful content creation. ",
        "ethics": "Key ethical issues include copyright, privacy, embedded social bias, over-reliance by students, and the risk that confident machine output may be trusted without verification. For a museum or school audience, the most important message is that LLM output should be treated as a draft or assistant, not as unquestionable truth. Human checking remains essential. ",
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
            },
            {
                "id": 18,
                "type": "image",    
                "url": "https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison",
                "title": "LLM Architecture Comparison",
                "caption": "Sebastian Raschka's overview comparing major LLM architectures"
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
                "id": 17,
                "title": "The Big LLM Architecture Comparison",
                "url": "https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison",
                "sourceType": "Article",
                "accessedDate": "2026-03-25",
                "notes": "Sebastian Raschka's overview comparing major LLM architectures"
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