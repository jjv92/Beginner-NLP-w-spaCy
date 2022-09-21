# Beginner-NLP-w-spaCy

!!!!READ ME!!!!

spaCy is a free, open-source library for advanced Natural Language Processing (nlp) in Python and Cython. 

spaCy is designed specifically for production use and helps you build applications that process and “understand” large volumes of text.

spaCy comes with pretrained pipelines and currently supports tokenization and training for 60+ languages. 
It features state-of-the-art speed and neural network model features such as: 
   1. tagging, 
   2. parsing, 
   3. named entity recognition, 
   4. text classification and more, 
   5. multi-task learning with pretrained transformers like BERT
It also functions as a production-ready training system and easy model packaging, deployment and workflow management. 

Major Features:
    1. Support for 60+ languages
    2. Trained pipelines for different languages and tasks
    3. Multi-task learning with pretrained transformers like BERT
    4. Support for pretrained word vectors and embeddings
    5. State-of-the-art speed
    6. Production-ready training system
    7. Linguistically-motivated tokenization
    8. Components for named entity recognition, part-of-speech-tagging, dependency parsing, sentence segmentation, text classification, lemmatization, morphological analysis, entity linking and more
    9. Easily extensible with custom components and attributes
    10. Support for custom models in PyTorch, TensorFlow and other frameworks
    11. Built in visualizers for syntax and NER
    12. Easy model packaging, deployment and workflow management
    13. Robust, rigorously evaluated accuracy

spaCy is available on PyPI and is downloaded the following way through pip in your terminal:
    pip install spacy

!It is recommended that before installing spaCy that you make sure that your pip, setuptools and wheel are up to date!
    enter the following to do so:
        pip install -U pip setuptools wheel

spaCy can be updated through entering the following commands into your terminal:
    pip install -U spacy
    python -m spacy validate

Trained language pipelines for spaCy can be installed as Python packages. 
This means that they're a component of your application, just like any other! 
Models can be installed using spaCy's download command, or manually by pointing pip to a path or URL.
    ex of the first method: 
        python -m spacy download en_core_web_lg
            **!!This package is needed to run the code in my python file**!!

    ex of the path and/or url methods:
        pip install /Users/you/en_core_web_lg-3.0.0.tar.gz
        pip install /Users/you/en_core_web_lg-3.0.0-py3-none-any.whl
        pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.0.0/en_core_web_lg-3.0.0.tar.gz

**How to Use the Attached Python File/Run the Code**:
    It is important to note that as previously stated, you need to install the "en_core_web_lg" lagnguage pipeline package
 
    You must also import spacy (to actually use the module) and displacy in order to properly execute the code.
	Method(s) seen below:

		import spacy
    			#import statement used to call upon the external/third party spaCy module into this program

		from spacy import displacy
    			#imports the spacy visualizer dependency 'displacy' which allows for in browser/notebook data visualization
**IMPORTANT CHANGE**
    In the following line of code, 
	'with open ("D:/Desktop/OOP Final/alice.txt", "r", encoding="utf8",) as f:'
    users willl have to replace certain parts of the file stream in order for the code to function on their device, ex: ("C:/Downloads/OOP Final/alice.txt")
	This manual change must be done to specify where the 'alice.txt' file is located so that it can be opened and read!!!
