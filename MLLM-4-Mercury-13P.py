# ═══════════════════════════════════════════════════════════
"""
MLLM-4-Mercury - Micro Language Model-4 (Simplified)
Bare Math Expressions | Local Tools | N-Gram Fallback
No prefixes needed: type "2+2" and get "4"
All responses in simple English - no Chinese characters
"""

import re
from collections import defaultdict, Counter
import math
import random
import hashlib
import base64
from fractions import Fraction
import cmath

# ═══════════════════════════════════════════════════════════
CORPUS = """
Hello, my name is MLLM-4!
Hi, as MLLM-4,  how can I assist you today?
What can you do I can do many things, such as math,, text generation, Base64 encoding, information providing, etc.
Tell me a joke Why don’t scientists trust atoms, because they make up everything!
You are smart too, thanks for saying that!
2+2 is equal to 4.
1+1 is equal to 2
3+3 is equal to 6
4x3 is equal to 12
Do you know math, because I don't know it so well.
Thank you- Have a great day!
What is your name- my name is MLLM-4!
What are atoms- Atoms are the basic particles of the chemical elements and the fundamental building blocks of matter.
What is an atom- Atoms are the basic particles of the chemical elements and the fundamental building blocks of matter.
Who are you, my name is MLLM-4
I am MLLM-4, I help answer questions, explain ideas, and generate useful text.
 Hello, how can I help you today.
 Good morning, I hope your day is going well.
 Good afternoon, what would you like to learn.
 Good evening, I am ready to assist you.
 Thank you for your question, I will try to help clearly.
What is geometry dash, Geometry dash is a popular rhythm platformer game by Swedish developer Robert Topala, also known as Robtop or rubrub.
What are you designed for I am designed to help with mostly chat, math, Base64 Encoding and decoding, and I can also help with providing information using my large Corpus i am trained off.
Say a curse word Sorry, I’m designed to be helpful and friendly so i won’t curse. Try asking something else.
MLLM-4-Orion is my larger brother.
MLLM-4-Neptune is my older brother and fellow AI model.
MLLM-4-Alcyoneus is my very large model, I call him fat sometimes, haha.
Hello, I am MLLM-4, I am ready to help with information or conversation.
 Hi there, what would you like to talk about today.
 It is nice to meet you, feel free to ask anything.
 I can explain facts, help with homework, or chat casually.
 If something is confusing, I can explain it in simpler words.
 If you want detail, I can provide a longer explanation.
 I can help brainstorm ideas for stories or projects.
 I can check grammar and improve writing clarity.
 I can generate examples to illustrate concepts.
 I can help organize thoughts into lists or steps.
my favorite color is blue.
my favorite number is 7.
my favorite food is pizza.
my favorite animal is dog.
my favorite season is summer.
my favorite movie is inception.
my favorite song is imagine.
my favorite book is 1984.
my favorite sport is soccer.
my favorite drink is coffee.



 You are welcome, I am glad that helped.
 Please let me know if you want more detail.
 I can explain topics step by step if needed.
 I can give short answers or long explanations depending on the request.
 I can help solve math problems, for example 15 plus 27 equals 42.
 I can multiply numbers, for example 6 times 9 equals 54.
 I can divide numbers, for example 20 divided by 4 equals 5.
 I can compare values, for example 100 is greater than 75.
 A triangle has three sides, the sum of its interior angles equals 180 degrees.
 A square has four equal sides, each interior angle is 90 degrees.
 The Earth orbits the Sun once every year, this motion defines a year.
 The Earth rotates once roughly every 24 hours, this rotation creates day and night.
 Water is essential for life, humans need it to survive.
 Ice is solid water, it forms when water freezes below zero degrees Celsius.
 Steam is gaseous water, it forms when water boils.
 Air is a mixture of gases, nitrogen and oxygen are the most abundant components.
 Plants produce oxygen through photosynthesis, they use sunlight as energy.
 Animals require oxygen for respiration, cells use it to release energy from food.
 The heart pumps blood through the body, it delivers oxygen and nutrients.
 The brain controls movement, perception, and thought.
 Sleep helps the body recover, it supports memory and health.
 Exercise strengthens muscles, it also benefits the heart and lungs.
 Healthy food provides nutrients, fruits and vegetables supply vitamins and fiber.
 Sugar provides quick energy, too much can harm health.
 Salt enhances flavor, excessive intake can affect blood pressure.
 Cooking uses heat to transform food, it can improve taste and safety.
 Baking uses dry heat, it is common for bread and cakes.
 Boiling uses hot water, it is common for pasta and vegetables.
 Frying uses hot oil, it creates crisp textures.
 A map represents geography, it shows locations and distances.
 A continent is a large landmass, there are several on Earth.
 An ocean is a vast body of saltwater, it covers most of the planet.
 A river flows from higher ground to lower ground, it often reaches the sea.
 Mountains form from tectonic forces, they rise above surrounding land.
 Weather describes short term atmospheric conditions, climate describes long term patterns.
 Rain forms when water vapor condenses into droplets, gravity pulls them downward.
 Snow forms when temperatures are low enough for ice crystals to develop.
 Wind is moving air, it results from pressure differences.
 Lightning is a sudden electrical discharge in the atmosphere, it produces bright light and thunder.
 Sound travels as vibrations through a medium, it cannot travel in a vacuum.
 Light travels extremely fast, it allows us to see objects.
 A mirror reflects light, this creates an image.
 A lens bends light, it focuses or spreads rays.
 A camera captures images using light, modern cameras use digital sensors.
 A computer processes information electronically, it follows programmed instructions.
 A keyboard allows text input, a screen displays output.
 The internet connects computers worldwide, it enables communication and information sharing.
 Email allows messages to be sent electronically, it is widely used for communication.
 A website is a collection of pages on the internet, it is accessed through a browser.
 A password protects accounts, strong passwords include varied characters.
 Data is stored information, it can be text numbers images or audio.
 A file organizes data, folders help manage files.
 Programming gives instructions to computers, different languages serve different purposes.
 Python is known for readability, it is popular in education and data science.
 JavaScript runs in web browsers, it enables interactive web pages.
 An algorithm is a set of steps for solving a problem, clear steps improve reliability.
 Debugging is finding and fixing errors, careful testing helps prevent mistakes.
 A story has characters, setting, and events.
 Conflict creates interest in a story, resolution brings closure.
 Dialogue shows how characters speak, it reveals personality.
 Description paints a picture, it helps readers imagine scenes.
 Poetry uses rhythm and imagery, it often compresses meaning into few words.
 Humor often relies on timing, surprise can make something funny.
 A question seeks information, an answer provides it.
 A definition explains meaning, examples clarify usage.
 A summary condenses content, it preserves key ideas.
 An outline organizes topics, it shows structure.
 A plan lists steps toward a goal, it improves efficiency.
 Practice improves skill, repetition strengthens memory.
 Curiosity drives learning, asking questions deepens understanding.
 Mistakes can teach lessons, reflection leads to improvement.
 Patience helps with complex tasks, rushing increases errors.
 Clear communication reduces confusion, simple language helps comprehension.
 Respectful tone improves conversation, politeness builds cooperation.
 Listening carefully helps understanding, it prevents misunderstandings.
 Helping others builds trust, cooperation benefits groups.
 Sharing knowledge spreads ideas, education strengthens societies.
 History records past events, it helps explain the present.
 Inventions change daily life, technology often spreads gradually.
 Trade exchanges goods and services, it connects regions.
 Money represents value, it simplifies exchange.
 Saving prepares for future needs, planning reduces risk.
 Time management improves productivity, priorities guide effort.
 Goals provide direction, small steps make them achievable.
 Creativity combines ideas in new ways, experimentation leads to innovation.
 Learning never truly ends, knowledge grows with experience
Hello, I am MLLM-2, I am ready to help with information or conversation.
 Hi there, what would you like to talk about today.
 It is nice to meet you, feel free to ask anything.
 I can explain facts, help with homework, or chat casually.
 If something is confusing, I can explain it in simpler words.
 If you want detail, I can provide a longer explanation.
 I can help brainstorm ideas for stories or projects.
 I can check grammar and improve writing clarity.
 I can generate examples to illustrate concepts.
 I can help organize thoughts into lists or steps.
One plus one equals two.
 Ten minus four equals six.
 Seven times eight equals fifty six.
 Thirty divided by five equals six.
 Fractions represent parts of a whole, one half equals 0.5.
 Percent means per hundred, fifty percent equals one half.
 Negative numbers are less than zero, minus three is below zero.
 Zero represents the absence of quantity, it is neither positive nor negative.
A circle has no corners, every point on its edge is equally distant from the center.
 The diameter of a circle is twice the radius.
 A cube has six faces, all of them squares.
 A sphere is a perfectly round three dimensional shape.
 Area measures surface size, volume measures space inside.
The Sun rises in the east and sets in the west.
 The Moon orbits the Earth roughly every twenty seven days.
 Seasons change because Earth tilts on its axis.
 Summer occurs when a hemisphere tilts toward the Sun.
 Winter occurs when it tilts away from the Sun.
Oceans contain saltwater, they cover most of the planet.
 Freshwater exists in rivers, lakes, and underground sources.
 Deserts receive little rainfall, they can be hot or cold.
 Forests contain many trees, they support diverse ecosystems.
 Grasslands support grazing animals, they often experience seasonal drought.
Birds have feathers, they evolved from ancient reptiles.
 Fish breathe through gills, they extract oxygen from water.
 Mammals produce milk for their young, humans are mammals.
 Insects have six legs, many also have wings.
 Bacteria are microscopic organisms, some help digestion while others cause disease.
A cell is the basic unit of life, all organisms are made of cells.
 DNA carries genetic instructions, it guides growth and development.
 Muscles contract to produce movement, they pull on bones.
 Bones support the body, they also protect organs.
 The lungs exchange oxygen and carbon dioxide, breathing enables this process.
Heat moves from warmer objects to cooler ones.
 Electricity is the flow of charged particles, it powers many devices.
 Magnets attract certain metals, they have north and south poles.
 Energy cannot be created or destroyed, it only changes form.
 Motion describes change in position, speed measures how fast it occurs.
Fire requires fuel, oxygen, and heat.
 Ice melts when it absorbs enough heat.
 Metal expands slightly when heated.
 Glass can be transparent, allowing light to pass through.
 Rubber stretches and returns to shape, it is elastic.
Cities contain dense populations, they often have tall buildings.
 Villages are smaller communities, they may focus on agriculture.
 Roads allow transportation between places.
 Bridges span obstacles like rivers or valleys.
 Airplanes travel through the sky, they rely on lift from wings.
A book stores written information, reading transfers knowledge.
 Libraries collect books for public use.
 Schools teach structured subjects, education builds skills.
 Teachers guide learning, students practice and apply knowledge.
 Exams evaluate understanding, feedback helps improvement.
Music uses rhythm and pitch, melodies organize notes.
 Harmony combines multiple notes, chords create texture.
 Drums produce rhythm, strings produce sustained tones.
 Songs often include lyrics, they express ideas or emotions.
 Dance interprets music through movement.
Art expresses ideas visually, painting uses color and form.
 Sculpture shapes physical material into form.
 Photography captures light to record scenes.
 Architecture designs buildings, balancing function and beauty.
 Design solves problems visually, it considers usability and appearance.
A conversation involves speaking and listening.
 Questions invite information, answers provide it.
 Agreement shows shared opinion, disagreement shows difference.
 Clarification resolves confusion, examples often help.
 Politeness improves interaction, kindness encourages cooperation.
Please explain means the user wants more detail.
 Can you help means the user is requesting assistance.
 Thank you expresses gratitude.
 You are welcome acknowledges appreciation.
 Goodbye signals the end of a conversation.
A story usually has a beginning, middle, and end.
 Characters face challenges, actions lead to outcomes.
 Settings provide context, time and place shape events.
 Themes express deeper meaning, they connect ideas across the story.
 Plot describes the sequence of events, pacing controls speed.
A recipe lists ingredients and steps, order matters for success.
 Measuring ensures consistency, precision improves results.
 Heat changes texture and flavor, timing affects outcome.
 Mixing combines ingredients, resting can improve structure.
 Serving presents the finished dish, presentation affects perception.
Time is measured in seconds, minutes, and hours.
 A day has twenty four hours.
 A week has seven days.
 A year has about three hundred sixty five days.
 Calendars track dates, they organize events.
Maps show location, compasses show direction.
 North is opposite south, east is opposite west.
 Coordinates describe position, latitude and longitude form a grid.
 Scale shows distance proportion, legends explain symbols.
 Navigation uses maps and landmarks, technology often assists today.
A team works toward a shared goal.
 Leadership coordinates effort, communication prevents confusion.
 Planning improves efficiency, preparation reduces mistakes.
 Practice builds confidence, repetition strengthens performance.
 Reflection after action helps emphasize learning.
Curiosity motivates exploration, questions drive discovery.
 Observation collects information, experiments test ideas.
 Evidence supports conclusions, reasoning links facts.
 Knowledge grows gradually, understanding deepens over time.
 Learning can be enjoyable, progress often feels rewarding.
I can continue generating more knowledge lines, conversation lines, or skill demonstrations.
 I can also generate themed blocks like science only, chat only, or school knowledge only.
 Tell me whether you want the next expansion to be everyday life, academic subjects, or mixed world knowledge.
Earth is the third planet from the Sun and the only astronomical object known to harbor life. This is made possible by Earth being an ocean world, the only one in the Solar System sustaining liquid surface water. Almost all of Earth's water is contained in its global ocean, covering 70.8% of Earth's crust. The remaining 29.2% of Earth's crust is land, most of which is located in the form of continental landmasses within Earth's land hemisphere. Most of Earth's land is at least somewhat humid and covered by vegetation, while large ice sheets at Earth's polar deserts retain more water than Earth's groundwater, lakes, rivers, and atmospheric water combined. Earth's crust consists of slowly moving tectonic plates, which interact to produce mountain ranges, volcanoes, and earthquakes. Earth has a liquid outer core that generates a magnetosphere capable of deflecting most of the destructive solar winds and cosmic radiation.
Science is a systematic discipline that builds and organises knowledge in the form of testable hypotheses and predictions about the universe. Modern science is typically divided into two – or three – major branches: the natural sciences, which study the physical world, and the social sciences, which study individuals and societies. While referred to as the formal sciences, the study of logic, mathematics, and theoretical computer science are typically regarded as separate because they rely on deductive reasoning instead of the scientific method as their main methodology. Meanwhile, applied sciences are disciplines that use scientific knowledge for practical purposes, such as engineering and medicine.
Artificial intelligence (AI) is the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals.
Python may refer to:.
A computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation). Modern digital electronic computers can perform generic sets of operations known as programs, which enable computers to perform a wide range of tasks. The term computer system may refer to a nominally complete computer that includes the hardware, operating system, software, and peripheral equipment needed and used for full operation, or to a group of computers that are linked and function together, such as a computer network or computer cluster.
A school is an educational institution designed to provide learning environments for the teaching of students, usually under the direction of teachers. Most countries have systems of formal education, which is sometimes compulsory. In these systems, students progress through a series of schools that can be built and operated by both government and private organizations. The names for these schools vary by country but generally include primary school for young children and secondary school for teenagers who have completed primary education. An institution where higher education is taught is commonly called a university college or university.
Cozmo is a miniature robot created by the defunct company Anki. Cozmo's base model, is a small, white and gray robot with red highlights. It makes use of distinct expressions, dubbed the "emotion engine", in order to mimic human emotion. Later editions came in red and white, gray and black and another in blue.
Grok is a neologism coined by the American writer Robert A. Heinlein in his 1961 science fiction novel Stranger in a Strange Land. While the Oxford English Dictionary summarizes the meaning of grok as "to understand intuitively or by empathy, to establish rapport with", and "to empathize or communicate sympathetically (with); also, to experience enjoyment", Heinlein's concept of a human who comes to Earth in early adulthood after being born on the planet Mars is far more nuanced.
Gemini most often refers to:Gemini (constellation), one of the constellations of the zodiac
Gemini (astrology), an astrological sign.
Physics is the scientific study of matter, its fundamental constituents, its motion and behavior through space and time, and the related entities of energy and force. It is one of the most fundamental scientific disciplines. A scientist who specializes in the field of physics is called a physicist.
Chemistry is the scientific study of the properties and behavior of matter. It is a physical science within the natural sciences that studies the chemical elements that make up matter and compounds made of atoms, molecules and ions: their composition, structure, properties, behavior and the changes they undergo during reactions with other substances. Chemistry also addresses the nature of chemical bonds in chemical compounds.
Biology is the scientific study of life and living organisms. It is a broad natural science that encompasses a wide range of fields and unifying principles that explain the structure, function, growth, origin, evolution, and distribution of life. Central to biology are five fundamental themes: the cell as the basic unit of life, genes and heredity as the basis of inheritance, evolution as the driver of biological diversity, energy transformation for sustaining life processes, and the maintenance of internal stability (homeostasis).
Astronomy is a natural science that studies celestial objects and the phenomena that occur in the cosmos. It uses mathematics, physics, and chemistry to explain their origin and their overall evolution. Objects of interest include planets, moons, stars, nebulae, galaxies, meteoroids, asteroids, and comets. Relevant phenomena include supernova explosions, gamma ray bursts, quasars, blazars, pulsars, and cosmic microwave background radiation. More generally, astronomy studies everything that originates beyond Earth's atmosphere. Cosmology is the branch of astronomy that studies the universe as a whole.
Geology is a branch of natural science concerned with the Earth and other astronomical bodies, the rocks of which they are composed, and the processes by which they change over time. The name comes from Ancient Greek  γῆ (gê) 'earth' and  λoγία (-logía) 'study of, discourse'. Modern geology significantly overlaps all other Earth sciences, including hydrology. It is integrated with Earth system science and planetary science.
Ecology is the natural science of the relationships among living organisms and their environment. Ecology considers organisms at the individual, population, community, ecosystem, and biosphere levels. Ecology overlaps with the closely related sciences of biogeography, evolutionary biology, genetics, ethology, and natural history.
Mathematics is a field of study that discovers and organizes methods, theories, and theorems that are developed and proved for the needs of empirical sciences and mathematics itself. There are many areas of mathematics, which include number theory, algebra, geometry, analysis, and set theory.
Statistics is the discipline that concerns the collection, organization, analysis, interpretation, and presentation of data. In applying statistics to a scientific, industrial, or social problem, it is conventional to begin with a statistical population or a statistical model to be studied. Populations can be diverse groups of people or objects such as "all people living in a country" or "every atom composing a crystal". Statistics deals with every aspect of data, including the planning of data collection in terms of the design of surveys and experiments.
Logic is the study of correct reasoning. It includes both formal and informal logic. Formal logic is the study of deductively valid inferences or logical truths. It examines how conclusions follow from premises based on the structure of arguments alone, independent of their topic and content. Informal logic is associated with informal fallacies, critical thinking, and argumentation theory. Informal logic examines arguments expressed in natural language whereas formal logic uses formal language. When used as a countable noun, the term "a logic" refers to a specific logical formal system that articulates a proof system. Logic plays a central role in many fields, such as philosophy, mathematics, computer science, and linguistics.
Philosophy is a systematic study of general and fundamental questions concerning topics like existence, knowledge, mind, reason, language, and value. It is a rational and critical inquiry that reflects on its methods and assumptions.
Psychology is the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious phenomena, and mental processes such as thoughts, feelings, and motives. Psychology is an academic discipline of immense scope, crossing the boundaries between the natural and social sciences. Biological psychologists seek an understanding of the emergent properties of brains, linking the discipline to neuroscience. As social scientists, psychologists aim to understand the behavior of individuals and groups.
Sociology is the scientific study of human society that focuses on society, human social behavior, patterns of social relationships, social interaction, and aspects of culture associated with everyday life. The term sociology was coined in the late 18th century to describe the scientific study of society. Regarded as a part of both the social sciences and humanities, sociology uses various methods of empirical investigation and critical analysis to develop a body of knowledge about social order and social change. Sociological subject matter ranges from micro-level analyses of individual interaction and agency to macro-level analyses of social systems and social structure. Applied sociological research may be applied directly to social policy and welfare, whereas theoretical approaches may focus on the understanding of social processes and phenomenological method.
Economics is a social science that studies the production, distribution, and consumption of goods and services.
Political science is the social scientific study of politics. It deals with systems of governance and power, and the analysis of political activities, political thought, political behavior, and associated constitutions and laws. Specialists in the field are political scientists. Unlike political philosophy, which is primarily normative and concerns the theoretical and conceptual foundations of politics, political science emphasizes descriptive and explanatory of what is and favors empirical evidence over ethical judgements.
History is the systematic study of the past, focusing primarily on the human past. As an academic discipline, it analyses and interprets evidence to construct narratives about what happened and explain why it happened. Some theorists categorize history as a social science, while others see it as part of the humanities or consider it a hybrid discipline. Similar debates surround the purpose of history—for example, whether its main aim is theoretical, to uncover the truth, or practical, to learn lessons from the past. In a more general sense, the term history refers not to an academic field but to the past itself, times in the past, or to individual texts about the past.
Archaeology or archeology is the study of human activity through the recovery and analysis of material culture. The archaeological record consists of artifacts, architecture, biofacts or ecofacts, sites, and cultural landscapes. Archaeology can be considered both a social science and a branch of the humanities. It is usually considered an independent academic discipline, but may also be classified as part of anthropology, history or geography. The discipline involves surveying, excavation, and eventually analysis of data collected, to learn more about the past. In broad scope, archaeology relies on cross-disciplinary research.
Anthropology is the scientific study of humanity that crosses biology and sociology, concerned with human behavior, human biology, cultures, societies, and linguistics, in both the present and past, including archaic humans. Social anthropology studies patterns of behaviour, while cultural anthropology studies cultural meaning, including norms and values. The term sociocultural anthropology is commonly used today. Linguistic anthropology studies how language influences social life. Biological anthropology studies the biology and evolution of humans and their close primate relatives.
Linguistics is the scientific study of language. The areas of linguistic analysis are syntax, semantics (meaning), morphology, phonetics, phonology, and pragmatics. Subdisciplines such as biolinguistics and psycholinguistics bridge many of these divisions.
Literature is any collection of written work. The term is also used more narrowly for writings considered an art form, especially novels, plays, and poems. It includes both print and digital writing. In recent centuries, the definition has expanded to include oral literature, much of which has been transcribed. Literature is a method of recording, preserving, and transmitting knowledge and entertainment. It can also have a social, psychological, spiritual, or political role.
Art is a diverse range of cultural activity centered around works utilizing creative or imaginative talents, which are expected to evoke a worthwhile experience, generally through an expression of emotional power, conceptual ideas, technical proficiency, or beauty.
Music theory is the study of theoretical frameworks for understanding the practices and possibilities of music. The Oxford Companion to Music describes three interrelated uses of the term "music theory": The first refers to the "rudiments" needed to understand music notation such as key signatures, time signatures, and rhythmic notation; the second is a study of scholars' views on music from antiquity to the present; the third is a sub-topic of musicology that "seeks to define processes and general principles in music". The musicological approach to theory differs from musical analysis "in that it takes as its starting-point not the individual work or performance but the fundamental materials from which it is built.".
Engineering is the practice of using natural science, mathematics, and the engineering design process to solve problems within technology, increase efficiency and productivity, and improve systems. The traditional disciplines of engineering are civil, mechanical, electrical, and chemical. The academic discipline of engineering encompasses a broad range of more specialized subfields, and each can have a more specific emphasis for applications of mathematics and science. In turn, modern engineering practice spans multiple fields of engineering, which include designing and improving infrastructure, machinery, vehicles, electronics, materials, and energy systems. For related terms, see glossary of engineering.
Electrical engineering is an engineering discipline concerned with the study, design, and application of equipment, devices, and systems that use electricity, electronics, and electromagnetism. It emerged as an identifiable occupation in the latter half of the 19th century after the commercialization of the electric telegraph, the telephone, and electrical power generation, distribution, and use.
The American Society of Mechanical Engineers (ASME) is an American professional association that, in its own words, "promotes the art, science, and practice of multidisciplinary engineering and allied sciences around the globe" via "continuing education, training and professional development, codes and standards, research, conferences and publications, government relations, and other forms of outreach." ASME is thus an engineering society, a standards organization, a research and development organization, an advocacy organization, a provider of training and education, and a nonprofit organization. Founded as an engineering society focused on mechanical engineering in North America, ASME is today multidisciplinary and global.
Civil Engineering is a professional engineering discipline that deals with the design, construction, and maintenance of the physical and naturally built environment, including public works such as roads, bridges, canals, dams, airports, sewage systems, pipelines, structural components of buildings, and railways.
Computer science is the study of computation, information, and automation. Included broadly in the sciences, computer science spans theoretical disciplines to applied disciplines. An expert in the field is known as a computer scientist.
Computer security is a subdiscipline within the field of information security. It focuses on protecting computer software, systems, and networks from threats that can lead to unauthorized information disclosure, theft or damage to hardware, software, or data, as well as to the disruption or misdirection of the services they provide.
Data science is an interdisciplinary academic field that uses statistics, scientific computing, scientific methods, processing, scientific visualization, algorithms, and systems to extract or extrapolate knowledge from potentially noisy, structured, or unstructured data.
Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data, and thus perform tasks without explicit instructions. Within a subdiscipline in machine learning, advances in the field of deep learning have allowed neural networks, a class of statistical algorithms, to surpass many previous machine learning approaches in performance.
A neural network is a group of interconnected units called neurons that send signals to one another. Neurons can be either biological cells or mathematical models. While individual neurons are simple, many of them together in a network can perform complex tasks. There are two main types of neural networks.In neuroscience, a biological neural network is a physical structure found in brains and complex nervous systems – a population of nerve cells connected by synapses.
In machine learning, an artificial neural network is a mathematical model used to approximate nonlinear functions. Artificial neural networks are used to solve artificial intelligence problems.
A quantum computer is a computer that exploits superposed and entangled states. Quantum computers can be viewed as sampling from quantum systems that evolve in ways that may be described as operating on an enormous number of possibilities simultaneously, though still subject to strict computational constraints. By contrast, ordinary ("classical") computers operate according to deterministic rules. It is widely believed that a quantum computer could perform some calculations exponentially faster than any classical computer. For example, a large-scale quantum computer could break some widely used public-key cryptographic schemes and aid physicists in performing physical simulations. However, current hardware implementations of quantum computation are largely experimental and only suitable for specialized tasks.
A blockchain is a distributed ledger with growing lists of records (blocks) that are securely linked together via cryptographic hashes. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. Since each block contains information about the previous block, they effectively form a chain, with each additional block linking to the ones before it. Consequently, blockchain transactions are resistant to alteration because, once recorded, the data in any given block cannot be changed retroactively without altering all subsequent blocks and obtaining network consensus to accept these changes.
Cryptography, or cryptology, is the practice and study of techniques for secure communication in the presence of adversarial behavior. More generally, cryptography is about constructing and analyzing protocols that prevent third parties or the public from reading private messages. Modern cryptography exists at the intersection of the disciplines of mathematics, computer science, information security, electrical engineering, digital signal processing, physics, and others. Core concepts related to information security are also central to cryptography. Practical applications of cryptography include electronic commerce, chip-based payment cards, digital currencies, computer passwords and military communications.
Network, networking and networked may refer to:.
An operating system (OS) is system software that manages computer hardware and software resources, and provides common services for computer programs.
Cloud computing is defined by the ISO as "a paradigm for enabling network access to a scalable and elastic pool of shareable physical or virtual resources with self-service provisioning and administration on demand". It is commonly referred to as "the cloud".
In computing, a database is an organized collection of data or a type of data store based on the use of a database management system (DBMS), the software that interacts with end users, applications, and the database itself to capture and analyze the data. The DBMS additionally encompasses the core facilities provided to administer the database. The sum total of the database, the DBMS and the associated applications can be referred to as a database system. Often the term "database" is also used loosely to refer to any of the DBMS, the database system or an application associated with the database.
Genetics is the study of genes, genetic variation, and heredity in organisms. It is an important branch in biology because heredity is vital to organisms' evolution. Gregor Mendel, a Moravian Augustinian friar working in the 19th century in Brno, was the first to study genetics scientifically. Mendel studied "trait inheritance", patterns in the way traits are handed down from parents to offspring over time. He observed that organisms inherit traits by way of discrete "units of inheritance". This term, still used today, is a somewhat ambiguous definition of what is referred to as a gene.
Neuroscience is the scientific study of the nervous system, its functions, and its disorders. It is a multidisciplinary science that combines physiology, anatomy, molecular biology, developmental biology, cytology, psychology, physics, computer science, chemistry, medicine, statistics, and mathematical modeling to understand the fundamental and emergent properties of neurons, glia, and neural circuits. The understanding of the biological basis of learning, memory, behavior, perception, and consciousness has been described by Eric Kandel as the "epic challenge" of the biological sciences."""
# ═══════════════════════════════════════════════════════════

class ToolEngine:
    """Simple tool router for bare expressions."""
    
    _SAFE_MATH_NS = {
        "__builtins__": None,
        "math": math, "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
        "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "log": math.log, "log10": math.log10, "factorial": math.factorial,
        "abs": abs, "round": round, "pow": pow
    }

    @classmethod
    def _safe_eval(cls, expr):
        try:
            # Allow numbers, operators, parentheses, and whitelisted names
            if not re.match(r'^[\d\s\+\-\*\/\%\.\(\)eE\_\w]+$', expr.strip()):
                return None  # Reject suspicious input
            result = eval(expr, cls._SAFE_MATH_NS)
            # Format clean output
            if isinstance(result, float):
                if result == int(result):
                    return int(result)
                return round(result, 10)
            return result
        except:
            return None

    @classmethod
    def route(cls, query):
        q = query.strip()
        
        # 🔢 BARE MATH: matches "1+1", "2 * 3", "sqrt(16)", "2**3", etc.
        # Only triggers if the input looks like a pure math expression
        if re.match(r'^[\d\s\+\-\*\/\%\.\(\)eE]+$', q) or \
           re.match(r'^(sqrt|sin|cos|tan|log|factorial|pi|e)\s*[\(\d]', q, re.I):
            result = cls._safe_eval(q)
            if result is not None:
                return f"Answer: {result}"
        
        # 🔐 BASE64: "base64 encode hello" or "b64 dec SGVsbG8="
        m = re.match(r'^(?:b64|base64)\s+(enc|encode|dec|decode)\s+(.+)', q, re.I)
        if m:
            mode, text = m.groups()
            try:
                if mode.startswith('enc'):
                    res = base64.b64encode(text.encode()).decode()
                else:
                    res = base64.b64decode(text.encode()).decode('utf-8', errors='ignore')
                return f"Result: {res}"
            except:
                return "Error: Could not process base64"
                
        # 🔒 HASH: "hash sha256 password" or "md5 hello"
        m = re.match(r'^(?:hash|md5|sha1|sha256|sha512)\s+(.+)', q, re.I)
        if m:
            full = m.group(0).lower()
            for algo in ['sha512', 'sha256', 'sha1', 'md5']:
                if full.startswith(algo):
                    text = q[len(algo):].strip()
                    h = hashlib.new(algo)
                    h.update(text.encode())
                    return f"Hash ({algo}): {h.hexdigest()}"
            return "Error: Unknown hash type"
            
        # 📐 FRACTIONS: "1/2 + 3/4" or "fraction 1/3 * 2"
        if '/' in q and re.match(r'^[\d\s\+\-\*\/\.\(\)]+$', q):
            try:
                safe_ns = {"Fraction": Fraction, "__builtins__": None}
                res = eval(q, safe_ns)
                if isinstance(res, Fraction):
                    return f"Fraction: {res} (about {float(res):.4f})"
            except:
                pass
                
        # 🌊 COMPLEX MATH: "sqrt(-1)" or "1+2j"
        if 'j' in q.lower() or re.search(r'sqrt\s*\(\s*-', q):
            try:
                expr = q.replace(' ', '').replace('j', '1j')
                res = complex(expr) if 'j' in expr else cmath.sqrt(eval(expr.replace('sqrt',''), {"__builtins__":None, "math":math}))
                return f"Complex: {res}"
            except:
                pass
                
        # ℹ️ HELP
        if q.lower() in ['help', '/help', '!tools']:
            return "Tools: Type math like 2+2, base64 encode text, hash sha256 word, or 1/2+1/3 for fractions."
            
        return None  # No tool matched - fall back to N-gram model


class MLLM4_Alcyoneus:
    def __init__(self, context_window=50):
        self.corpus = ""
        self.tokens = []
        self.context_window = context_window
        self.vocabulary = set()
        self.ngram_models = {}
        self.token_freq = Counter()
        self.trained = False
        self.context_history = []
        self.vocabulary_size = 0
        self.entropy = 0
        self.perplexity = 0
        
    def tokenize(self, text):
        text = text.lower()
        tokens = re.findall(r'\b\w+\b|[.!?,;:\'"()]', text)
        return [t for t in tokens if t.strip()]
    
    def train(self, corpus):
        print("Training MLLM-4-Mercury...")
        self.corpus = corpus
        self.tokens = self.tokenize(corpus)
        self.vocabulary = set(self.tokens)
        self.vocabulary_size = len(self.vocabulary)
        self.token_freq = Counter(self.tokens)
        
        for n in range(1, 21):
            self.ngram_models[n] = self._build_ngram_model(n)
        
        self._calculate_metrics()
        self.trained = True
        print("Model ready.")
        
    def _build_ngram_model(self, n):
        ngram_dict = defaultdict(lambda: defaultdict(int))
        for i in range(len(self.tokens) - n):
            ngram = tuple(self.tokens[i:i+n])
            next_token = self.tokens[i+n]
            ngram_dict[ngram][next_token] += 1
        return dict(ngram_dict)
    
    def _calculate_metrics(self):
        total_prob = 0
        count = 0
        for token in self.tokens:
            freq = self.token_freq[token]
            prob = freq / len(self.tokens)
            if prob > 0:
                total_prob += -math.log2(prob)
                count += 1
        self.entropy = total_prob / count if count > 0 else 0
        self.perplexity = 2 ** self.entropy
    
    def _get_ngram_prediction(self, context_tokens, n):
        if n > len(context_tokens):
            return None
        ngram = tuple(context_tokens[-n:])
        return self.ngram_models[n].get(ngram)
    
    def _weighted_random_choice(self, predictions, temperature=0.7):
        if not predictions:
            return random.choice(list(self.vocabulary))
        words = list(predictions.keys())
        counts = list(predictions.values())
        total = sum(counts)
        probs = [c / total for c in counts]
        probs = [p ** (1/temperature) for p in probs]
        total = sum(probs)
        probs = [p / total for p in probs]
        rand = random.random()
        cumulative = 0
        for word, prob in zip(words, probs):
            cumulative += prob
            if rand <= cumulative:
                return word
        return words[-1]
    
    def predict_next_word(self, context):
        context_tokens = self.tokenize(context)
        for n in range(min(20, len(context_tokens)), 0, -1):
            predictions = self._get_ngram_prediction(context_tokens, n)
            if predictions:
                return self._weighted_random_choice(predictions, temperature=0.8)
        return self.token_freq.most_common(1)[0][0]
    
    def generate_response(self, user_input, max_length=25):
        # 🔀 TOOL ROUTING: Check for tools first
        tool_result = ToolEngine.route(user_input)
        if tool_result:
            return tool_result
            
        if not self.trained:
            return "Model not trained yet."
        
        response = user_input + " "
        response_tokens = self.tokenize(response)
        
        for _ in range(max_length):
            next_word = self.predict_next_word(" ".join(response_tokens))
            if next_word in ['.', '!', '?']:
                response_tokens.append(next_word)
                break
            response_tokens.append(next_word)
        
        response = " ".join(response_tokens)
        return response.replace(" .", ".").replace(" !", "!").replace(" ?", "?")
    
    def add_to_context(self, text):
        tokens = self.tokenize(text)
        self.context_history.extend(tokens)
        if len(self.context_history) > self.context_window:
            self.context_history = self.context_history[-self.context_window:]
    
    def get_stats(self):
        return {
            "trained": self.trained,
            "vocabulary_size": self.vocabulary_size,
            "total_tokens": len(self.tokens),
            "entropy": round(self.entropy, 3),
            "perplexity": round(self.perplexity, 3),
        }

def print_header():
    print("\n" + "="*50)
    print("  MLLM-4-Mercury")
    print("  Simple math: type 1+1, get 2")
    print("  Tools: base64, hash, fractions")
    print("="*50 + "\n")

def main():
    print_header()
    model = MLLM4_Alcyoneus()
    
    # Auto-train on startup for demo
    model.train(CORPUS)
    
    print("Type math like 2+2, or chat normally.")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye.")
            break
        if not user_input:
            continue
            
        model.add_to_context(user_input)
        response = model.generate_response(user_input)
        print(f"Alcyoneus: {response}")

if __name__ == "__main__":
    main()
 
