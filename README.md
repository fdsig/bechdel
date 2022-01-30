## Bechdel Testing: Using Boolean Logic and BERT to predict whether a film script will pass the Bechdel test.

![image info](super_woman.png)

#### There are two parts to this:
1. An example of training software to train a binary NLP classifier (BERT) using twitter data split into male and female to clasify script text.

2. A notebook which evaluates condition one of Alison Bechdel's test calculated by comparing names in script with [male](https://www.cs.cmu.edu/Groups/AI/areas/nlp/corpora/names/female.txt) and [female](https://www.cs.cmu.edu/Groups/AI/areas/nlp/corpora/names/female.txt) first names  as a proxy for condition 1 and seeks to reject/confirm whether:
   >  - Consecutive first names of characters are an adequate proxy for meeting condition 1 of the Bechdel test **AND** if:
   >  - Films that pass condition 1 of the bechdel test using above methodology is a good predictor of passing all three conditions.

These hypotheses are tested using ground truth of [films that have been verified](https://bechdeltest.com/) to pass the Bechdel test. Failure of above hypothesis(acceptance of a null hypothesis) indicates whether there is a case for using more complex methods such as training an NLP model (for which code is also provided).

Further analysis of other proxies that can be used in a logical/computational approach are however needed, such as examining prevalence of male names that are the subject of sentences used in female to female dialogue (conditions 2 and 3 of Bechdel test) as well as examining the durational element of conversation between female characters.
 
**Bechdel criteria:**
- 1. [x] (of film or literature) Has to have at least two women (discrete/integer)**AND**;
- 2. [x] Talk to each other in (continuous time) **AND**;
- 3. [x] Talk about something other than a man (binary).

**Instructions to run notebook:**

Make new/install virtual environment (mac/linux) with:

```bash
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv env
```
Run notebook in venv and install dependencies: 

```bash
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
**Instructions to run training software:**

Note -- this is an illustrative work in progress rather than completed software. However, it will run , log in to Hugging Face AutoNLP  account and upload formatted data to Hugging Face AutoNLP. (A little more work would be required to train a binary classifier)

As above however if running in terminal run activated venv with dependencies and in project main directory:

For a list of possible flags to passable args run:

```bash

 python main.py --help

```
To log in to Hugging Face AutoNLP Run:

```bash
python3 main.py --hugging_face --login --api_key #yourapikey
```


To make a new project on AutoNLP:

```bash
python3 main.py  --make  #your make args here (eg. Binary_classification, multi_class)
```

To send data to AutoNLP:

```bash
python3 main.py  --send  #your data .csv args here
```

```bash
python3 main.py --train #your train args here
```
You will need:

> 1. A Hugging Face [AutoNLP](https://huggingface.co/autonlp) account;
> 2. Your Hugging Face AutoNLP API key;
> 3. Train csv with binary labelled text data parsed from [twitter_gender_classification.csv](https://www.kaggle.com/nisasoylu/nlp-for-twitter-gender-classification-nisa/data).

Depending on your OS there may be other AutoNLP (sub) dependencies when install requirments.txt these will most likely be flagged for further info see [AutoNLP](https://github.com/huggingface/autonlp) GitHub repository. (a very interesting project in its own right)


