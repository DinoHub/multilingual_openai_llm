Conda env: custom_loss
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
