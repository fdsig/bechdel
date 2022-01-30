## Bechdel test
![image info](super_woman.png)

#### There are two parts to this:
1. An example of training sofware to train a binary classifier using twitter data split into male and female to clasify script text.

2. A notebook which evaluates condition one of bechdel test calculated by comparing names in script with male and female names and verifies against ground truth of films that have been verified to pass the bechdel test.
 
**bechdel criteria:**
- 1. [x] (of film or literature) Has to have at least two women (discrete int) or $\in \mathbb{Z}$
- 2. [x] Talk to each other in (continuous time) or $\in \mathbb{R}$
- 3. [x] Talk about somthing other than a man (not.self) (binary) or $\in \mathbb{B}$ 

**instructions to run notebook**:

make new virtual environment (mac/linux) with:

```bash
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

```
Run notebook in vnv

**Instructions to run training software**

Note -- this is an illustrative work in progress rather than completed software. However will run and and log in to hugging face account and upload formatted data to hugging face. (A little more work would be required to train a binary classifier) 

As above however if running in terminal run 

In activated env virtual and in project main directory 

For list of possible flags:

```bash
python main.py -help 

```

You will need:

1. A hugging face account;
3. Your hugging face API key;
4. Train csv with binary labeled text data.

> README.md edited on phone ++ I am dyslexic:: (apologies for typos). 

