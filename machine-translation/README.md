Conda env: custom_loss

tir: /projects/tir6/general/aogayo/models/bloom/lti-llm-deployment/
# Generating Parallel Data
Language: Kiswahili - English. Why, I understand them.

## Queries and their responses
```
instruct ="Here is a list of places: Migori, Suneka, Kisii, Nyamira. Create sentences in Kiswahili using those towns."
Output: 
1. Mimi niko Migori.
2. Mimi niko Suneka.
3. Mimi niko Kisii.
4. Mimi niko Nyamira.
```
```
instruct ="Here is a list of places: Migori, Suneka, Kisii, Nyamira. Create sentences in Kiswahili using those towns and their translations in English."

1. Migori ni mji wa Kenya. - Migori is a town in Kenya.
2. Suneka ni mji wa Kenya. - Suneka is a town in Kenya.
3. Kisii ni mji wa Kenya. - Kisii is a town in Kenya
```
```
instruct ="Here is a list of places: Migori, Suneka, Kisii, Nyamira. Create sentences in Kiswahili using those towns and their translations in English. The sentences should be varied in meaning, topic, and structure."

1. Migori ni mji wa kusini mwa Kenya. (Migori is a town in the south of Kenya.)
2. Nyamira ni mji wa karibu na Migori. (Nyamira is a town close to Migori.)
```
```
instruct ="Here is a list of places: Migori, Suneka, Kisii, Nyamira. Create sentences in Kiswahili using those towns and their translations in English. The sentences should be varied in meaning, topic, and structure. They should include different styles also such as questions, dialogues etc."

1. "Je, unaenda wapi, Migori au Suneka?" - "Where are you going, Migori or Suneka?"

2. "Ninaenda kwenda Kisii leo." - "I'm going to Kisii today."
```
```
instruct ="Here is a list of places: Migori, Suneka, Kisii, Nyamira. Create sentences in Kiswahili using those towns and their translations in English. The sentences should be varied in meaning, topic, and structure. They should include different styles also such as questions, dialogues etc.The sentence and its translation should be tab separated"

Mimi niko katika Migori | I am in Migori |
Je, unaenda kwenda Suneka? | Are you going to Suneka? |
Ninaenda kwenda Kisii | I am going to Kisii |
Tun
```
The next prompt was constructed with the help of chatGPT. Prompt given to chatGPT
```
prompt: Write me a prompt that will tell a student to construct sentences with varied styles, structure, and meaning using some words that I have given them.
response: "Create four unique and well-constructed sentences using the following words: 'dog', 'ran', 'quickly', 'park'. Try to use varied sentence structures and meanings to showcase your understanding of language. For example, one sentence could be a simple statement, another a complex compound sentence, another a question, and the fourth an exclamation."
```
Now for the actual prompt:

```
instruct ="Here is a list of places: Migori, Suneka, Kisii, Nyamira." \
          " Create unique and well-constructed sentences in Kiswahili and their English translations using those towns." \
          " Try to use varied sentence structures and meanings to showcase your understanding of language. " \
          "For example, one sentence could be a simple statement, another a complex compound sentence, another a question, and the fourth an exclamation."
1. Migori, Suneka, Kisii na Nyamira ni miji mirefu sana! - Migori, Suneka, Kisii, and Nyamira are very far away!
2. Wapi unaenda kutembea kati ya Migori na Nyamira? - Where do you go travelling between Migori and Nyamira?
3. Miji ya Kisii na Suneka ni magharibi mno! - The towns of Kisii and Suneka are very far west!
4. Miji ya Migori, Suneka, Kisii na Nyamira ni miji mazuri sana! - The towns of Migori, Suneka, Kisii, and Nyamira are very nice places!

```
