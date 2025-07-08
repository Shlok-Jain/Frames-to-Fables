
# <center>Assignment 6 Documentation and Experimentation

##  <center><b>Team McMuffins
<center> Naina Bhalla  ||  Rohan Singhal  ||  Shivam Bansal<br></b>
</center>

---

## **Objective**

To explore different pre-trained image captioning models and generate a coherent story using the generated captions with the help of an LLM.

---

## **Dataset**

It consists of 4 static illustrations of two boys and their mother.<br>
![{D49AB54B-E88F-4ABF-B0CA-0312E1F4FBF9}](https://github.com/user-attachments/assets/a77015cf-f08e-434b-b39f-6db5168232aa)


> **Note:**
> All the images were fetched using `requests` and processed using `PIL`.

---

## **Part 1: Image Captioning**

### **Models Explored**

| Model                            | Pros                                                                | Cons                                                                 |
| -------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Salesforce BLIP**              | Lightweight compared to BLIP-2                                      | Lesser detailed than BLIP-2                                          |
| **Salesforce BLIP-2 (OPT 2.7B)** | Reliable and generates summarized accurate descriptions             | Heavy memory usage                                                   |
| **ViT-GPT2**                     | Lightweight                                                         | Poor contextual understanding and generates irrelevant/wrong details |
| **Kosmos-2**                     | Good for identifying specific activities, such as fighting, playing | May over-interpret scenes, slower processing                         |
| **Florence-2 Flux Large**        | Well-balanced in terms of identification and detail                 | Large model, requires significant memory, limited emotional context  |
| **GIT Large TextCaps**           | Great at object recognition and room-settings                       | Large model, occasional misinterpretation of scenes                  |
| **GPT-4.1**                      | Extremely detailed and comprehensive with better storytelling       | Requires API (cost incurred)                                         |

📄 **Captions Spreadsheet:** [**Link**](https://docs.google.com/spreadsheets/d/1xUHOMEAHV3YtCTMNm_mHaOGSS4njBah99ElICd_UmTc/edit?gid=0#gid=0)
> The final captions chosen for story generation were from **GPT-4.1**, as they were the most accurate and contextually rich.

---

## **Part 2: Story Generation**

### **LLMs Used**

| Model                | Story Link    |
| -------------------- | ------------- |
| **Gemma2-9b-it**     | [Story Link](#gemma2-9b-it) |
| **Llama3-8b-8192**   | [Story Link](#llama3-8b-8192) |
| **Deepseek-R1**      | [Story Link](#deepseek-r1-distill-llama-70b) |
| **OpenAI GPT-4o**    | [Story Link](#openai-gpt-4o) |
| **Gemini-2.0 Flash** | [Story Link](#gemini-flash-20) |
| **Mistral AI**       | [Story Link](#mistral-ai-latest) |

---

## **Stories Generated**

### **Gemma2-9b-it**

>

<details>
<summary>Click to expand full story</summary>

The red toy airplane was a prized possession, a symbol of adventure and daring for eight-year-old Leo, who clutched it tightly in his hand.  His younger brother, six-year-old Ethan, wanted the plane just as badly, his eyes flashing with a mixture of longing and frustration. They stared at each other, their faces inches apart, the cozy living room suddenly feeling like a battleground.  Leo, in his green tank top and blue shorts, pulled the airplane closer, a deep frown etched on his face. Ethan, dressed in an orange shirt and green shorts, refused to let go, his small hand gripping the toy with surprising strength. The air crackled with tension, unnoticed by their mother who was busy washing dishes at the kitchen sink, humming a cheerful tune.

Suddenly, a loud crack echoed through the room, followed by a gasp from Ethan. Leo froze, his eyes wide with horror as he saw the red airplane lying in pieces on the floor. The once vibrant toy was now a mangled mess, its wings broken and its body snapped in two. Ethan sank to his knees, tears welling up in his eyes. He buried his face in his hands, his sobs echoing through the living room.  

Leo's initial shock turned to guilt. He hadn't meant to break Ethan's favorite toy. He knelt beside his brother, his own face pale, and stammered an apology.  Their mother, alerted by the commotion, rushed into the living room, her face contorting with anger. Steam seemed to be literally billowing from her ears, her green oven gloves clenched into fists.

"What happened here?!" she exclaimed, her voice sharp with frustration.

The sight of his shattered toy and his brother's heartbroken sobs softened the anger in Leo's mother's eyes. She knelt beside Ethan, gently wiping away his tears. Then, she turned to Leo, her voice softer now. "It was an accident, sweetie," she said, her voice soothing. "We all make mistakes. But the important thing is to learn from them."

The next day, a new peace settled over the living room. Their mother, ever the resourceful one, had gathered colorful sheets of paper and sat down with the boys at the table.  Ethan, his sadness replaced with a spark of curiosity, watched as Leo, his green tank top replaced with a green sleeveless shirt, folded a vibrant red paper plane.  

"See, Ethan," Leo said, his voice a little quieter now, "you can make your own airplane! It can be even better than the old one."

Ethan’s eyes widened, and a small smile crept onto his face.  He picked up a sheet of yellow paper, following Leo's every move. The air, once thick with tension, now buzzed with the quiet click of paper being folded, the soft murmur of their voices as they shared tips and tricks.  

Later that afternoon, the living room was alive with the joyous whoosh of paper airplanes soaring through the air.  Leo, his green shirt replaced with a green and blue striped one, launched a red paper plane, its wings catching the sunlight. Ethan, in his orange T-shirt, laughed with delight as his yellow plane dipped and swerved through the air. Their mother, watching from the doorway, smiled. The broken toy had brought them together, not just as brothers, but as creators, inventors, and pilots of their own little paper airplane adventures.


</details>

---

### **Llama3-8b-8192**

>

<details>
<summary>Click to expand full story</summary>

The sun was shining brightly through the pink curtains of the living room, casting a warm glow over the cozy space. The sound of dishes being washed in the kitchen sink filled the air as the two young boys, Timmy and Tommy, engaged in a heated argument over a red toy airplane. Timmy, wearing a green tank top and blue shorts, pulled the toy towards himself, his eyes blazing with determination. Tommy, dressed in an orange shirt and green shorts, stood firm, refusing to give up his prized possession.

Their mother, Mrs. Johnson, was oblivious to the conflict, too engrossed in her chores to notice the commotion. But as the argument escalated, it was only a matter of time before things took a turn for the worse. In a moment of frustration, Tommy's grip on the toy airplane slipped, and it crashed to the floor, breaking into pieces.

Little Timmy's eyes welled up with tears as he stared at the broken toy, his face contorted in anguish. His mother, storming into the room, was shocked by the scene before her. "What's going on here?" she demanded, her voice stern and firm. Tommy, realizing his mistake, looked up at his mother with a mix of guilt and fear, while Timmy simply wailed, his heart heavy with disappointment.

As the tension in the room mounted, Mrs. Johnson tried to intervene, but it was clear that the damage was done. In the midst of the chaos, Tommy felt a pang of regret and guilt, knowing he had broken his brother's toy. He looked at Timmy's tear-stained face and felt a deep sense of sorrow.

But as the storm began to clear, Mrs. Johnson had an idea. "Why don't we make some new airplanes?" she suggested, her tone softening. "We can use paper and make some brand new ones!" Timmy's eyes lit up at the prospect, and Tommy's guilt began to fade, replaced by a sense of excitement and possibility.

Together, the three of them sat down at the round table, surrounded by colorful sheets of paper. As they worked, the tension in the room dissipated, replaced by the warmth and joy of creativity. Timmy and Tommy chatted and laughed, their differences forgotten in the face of their shared activity.

As they folded and crafted their paper airplanes, the living room filled with the sounds of laughter and chatter. Mrs. Johnson smiled, watching her sons work together, their bond growing stronger with each passing moment. And as they played, the broken toy airplane was all but forgotten, replaced by a sense of unity and togetherness.

In the end, it was clear that sometimes, even the most difficult moments can lead to something beautiful. As the sun continued to shine through the pink curtains, Timmy, Tommy, and their mother sat together, surrounded by the fruits of their labor – a mountain of colorful paper airplanes, each one a symbol of forgiveness, creativity, and the power of family.


</details>

---

### **Deepseek-r1-distill-llama-70b**

>

<details>
<summary>Click to expand full story</summary>

Once upon a time, in a cozy little house with a pink-curtained window and a warm, inviting living room, lived two young boys who were as close as brothers could be. Their names were Tommy and Timmy, and they shared a love for adventure, toys, and imagination. But like all siblings, they had their moments of disagreement.

One sunny afternoon, Tommy and Timmy found themselves in the middle of a heated argument. The source of their quarrel? A small, shiny red toy airplane. Tommy, wearing his green tank top and blue shorts, had been playing with it all morning, and Timmy, in his bright orange shirt and green shorts, had grown desperate to take a turn. The two boys tugged at the toy, their faces red with determination, each refusing to let go.

Meanwhile, their mother was in the kitchen, scrubbing dishes at the sink, oblivious to the storm brewing behind her. The room was filled with the usual sounds of a family home—the clink of dishes, the occasional chirp of a bird outside the window, and the muffled voices of the boys as they argued. But as the tension between them grew, the silence in the room became thick and heavy.

In the heat of the moment, disaster struck. The toy airplane, caught in their fierce tug-of-war, slipped from their grasp and crashed to the floor. It broke into pieces, its bright red wings bent and twisted beyond repair. Timmy, who had been so desperate to play with it, burst into tears, covering his face with his hands. Tommy, realizing what had happened, stood frozen in shock, his eyes wide with regret.

Their mother, hearing the commotion, turned from the sink, her hands still dripping with water. She was met with the sight of her two sons—one crying uncontrollably and the other looking like he had seen a ghost. Her expression shifted from surprise to frustration, and she let out a deep sigh. "What happened here?" she asked, her voice firm but laced with a hint of weariness.

Tommy hesitated, then pointed at the broken toy. "It was an accident!" he exclaimed, his voice trembling. "We were just playing, and it broke!"

Their mother shook her head, her hands on her hips. "An accident? Look at the mess you two made! That toy was Timmy's favorite, and now it's ruined!" Timmy wailed even louder at her words, and Tommy looked down at his feet, feeling guilty.

But then, something shifted. Their mother took a deep breath and knelt down beside them. "You know, boys," she said gently, "toys can be fixed, but feelings can't. What's important is how we handle this." She looked at Tommy. "Tommy, why don't you help Timmy make something even better than that toy? Something you both can play with together."

Tommy's eyes lit up at the idea. He glanced at Timmy, who sniffled but nodded slowly. Together, they went to the round table in the corner of the room, where colorful sheets of paper and scissors lay scattered. Their mother smiled as she watched them sit down, the tension in the room beginning to lift.

As the afternoon sun streamed through the window, the boys set to work. Tommy, with his quick hands, began folding a yellow sheet of paper into the shape of an airplane. Timmy, his tears forgotten, watched with wide eyes as Tommy explained each step. "See, Timmy? You gotta fold it just right so it flies straight!" he said, grinning. Timmy giggled and tried to mimic his brother's movements, his fingers fumbling but determined.

Before long, the table was covered in paper airplanes of all colors—red, yellow, purple, and more. The boys worked together, laughing and chatting, their earlier argument a distant memory. Their mother, now smiling, leaned against the doorway, watching her sons with pride. "You two are quite the team," she said, her voice soft and warm.

Finally, the moment of truth arrived. The boys stood up, each holding their newly made airplanes. Tommy aimed his first, launching it across the room with a whoosh. It soared gracefully before landing on the soft cushion of the sofa. Timmy clapped, his eyes shining with delight. "Your turn!" Tommy said, nudging his brother. Timmy took a deep breath, threw his airplane, and watched as it glided through the air, spinning in circles before coming to rest near the window.

The boys laughed, their joy filling the room. Their mother joined in, her earlier frustration replaced by a sense of contentment. "You know," she said, "sometimes when things break, we can make something even better. And when we work together, nothing is impossible."

As the sun dipped lower, casting a golden glow through the pink curtains, the boys continued to play, their paper airplanes fluttering through the air like tiny, colorful birds. The broken toy was forgotten, replaced by something far more valuable—a lesson in sharing, forgiveness, and the magic of creation.

And so, in that cozy little house, life went on, filled with laughter, love, and the endless possibilities of a child's imagination.

</details>

---

### **OpenAI-GPT-4o**

>

<details>
<summary>Click to expand full story</summary>

Once upon a time, in a cozy family home, two young brothers, Tommy and Jake, found themselves at odds over a beloved possession—a bright red toy airplane. Tommy, the older brother, dressed in a green tank top and blue shorts, had his eyes set on the plane, tugging vigorously with a determination only seen in a child defending his treasure. Jake, the younger, equally determined and dressed in an orange shirt with green shorts, mirrored his brother's energy. Their voices rose in a crescendo of youthful indignation, each boy convinced that the airplane should be his.

Their mother, Michelle, was busily engaged at the kitchen sink, her attention absorbed by the cascade of bubbles that accompanied the evening's dishwashing. The living room was softly lit, the window dressed with pink curtains framing a gentle glow that embraced the home’s serene semblance—serene except for the brewing storm behind her.

As the minutes passed, the siblings' tug-of-war reached its climax. With one final pull from each, the airplane succumbed to their struggle, snapping into pieces with a sound that echoed their mutual dismay.

Tommy’s reaction was immediate. Shock mixed with guilt washed over his features, leaving him momentarily speechless. Jake, however, expressed his grief openly. Tears streamed down his cheeks as he buried his face in his hands, his small shoulders shaking with sobs over the tragedy of his broken toy. Michelle, alerted by the sudden silence followed by a wail, turned around. Her expression quickly shifted from confusion to exasperation as she rushed into the living room.

The sight that greeted her was enough to make steam figuratively rise from her head. With hands planted firmly on her hips, Michelle surveyed the scene—the shattered airplane, Jake’s tears, and Tommy’s uneasy stance pointed toward an unwelcome conclusion. Her voice was firm but compassionate as she inquired into the series of unfortunate events, seeking resolution more than reprimand.

Later, in the same cozy setting, a different atmosphere prevailed. A lesson in patience and understanding had been learned, and it blossomed into a new endeavor—creating paper airplanes. Tommy, now wearing a green sleeveless shirt with a white star, had taken the lead in turning the misadventure into a moment of bonding. His fingers deftly folded the colorful sheets of paper, explaining with earnest enthusiasm the art of making the perfect paper airplane.

Jake, eager to divert his creative energy, listened intently, his eyes wide with the wonder of new knowledge. Together they crafted a fleet of vibrant aircraft, red and yellow, purple and blue, ready to soar on imaginary winds. The table was a testament to their creative spirits, scattered with hues as bright as their renewed sibling camaraderie.

Finally, with their paper fleet assembled, Tommy and Jake returned to the living room with their mother watching from the doorway, her earlier anger replaced by a gentle smile. The boys spiraled into laughter as they aimed and launched their paper creations, filling the air with fluttering colors.

The sunlight streamed through the window, casting a warm glow on the scene that unfolded—a living room now full of giggles and forgotten grievances. Nearby, the remnants of the broken toy airplane lay, its purpose fulfilled; it had been the catalyst for a day filled with lessons of sharing, forgiveness, and the joys of creating together.

And there, in the colored chaos of their play, the home felt whole once again, with the echoes of brotherhood bouncing from wall to wall, a reminder that sometimes joy can wing its way into our hearts on the simplest of paper planes.



</details>

---

### **Gemini-Flash-2.0**

>

<details>
<summary>Click to expand full story</summary>

The red toy airplane, a prized possession in their shared world, became the epicenter of a fierce battle. Ten-year-old Leo, in his favorite green tank top, gripped the wing, his knuckles white. Opposite him, eight-year-old Finn, clad in an orange shirt, mirrored his intensity, his face a mask of stubborn determination. "It's my turn, Leo! You had it all morning!" Finn's voice was tight with frustration. Leo retorted, "But I was just about to make it fly through the tunnel!" Their voices rose, the argument escalating, oblivious to the rhythmic clatter of dishes from the kitchen sink where their mother, Sarah, was lost in her afternoon chores, unaware of the brewing storm behind her. The cozy living room, usually a haven of laughter and games, now felt charged with animosity.

The inevitable happened. A sharp tug, a sickening crack, and the red airplane lay broken on the worn rug. Finn burst into tears, his small hands covering his face, his shoulders shaking with sobs. Leo, aghast at the sight of the mangled toy, could only stammer, "I...I didn't mean to!" Sarah, alerted by the commotion, stormed in, her face a thundercloud. Steam practically billowed from her ears as she placed her hands on her hips, green gloved hands still damp from dishwater. "What in the world is going on here?" she demanded, her voice sharp with exasperation. The broken airplane was a testament to their squabble, and the sight of Finn's distress was the last straw.

Later that week, determined to foster peace and creativity, Sarah brought out a stack of colorful construction paper. "Let's make something new," she announced, placing the pile on the round table in the living room. Leo, remembering Finn's tears and his mother's displeasure, approached the table cautiously. Soon, both boys were engrossed in folding and creasing, transforming flat sheets of paper into soaring paper airplanes. Leo, ever the showman, demonstrated the perfect fold for maximum flight, his green sleeveless shirt revealing a white star on the front. Finn, his orange T-shirt a splash of brightness, watched with rapt attention, his initial sadness replaced with a spark of excitement. Red, yellow, and purple paper airplanes began to populate the table, symbols of their newfound camaraderie.

Days later, the living room was filled with joyous whoops and laughter. Paper airplanes of every hue darted through the air, launched by two beaming boys. Leo, in his green shirt and blue shorts, aimed a red paper airplane towards an imaginary target, while Finn, his orange shirt a beacon of happiness, watched with wide-eyed glee. The tension of the past was completely forgotten, replaced by the simple pleasure of play. Sarah, standing in the doorway, her face softened with a warm smile, watched her sons with pride. The sunlight streamed through the pink curtains, illuminating the scene, and the aroma of baking bread wafted from the kitchen, completing the picture of a happy, harmonious home. The broken red airplane was a distant memory, replaced by the vibrant, colorful world they had created together.




</details>

---

### **Mistral-AI-Latest**

>

<details>
<summary>Click to expand full story</summary>

In the heart of a cozy family home, two young boys, Jake and Lucas, were engrossed in a tense standoff. The object of their dispute? A gleaming red toy airplane, a treasure that had brought them joy and imaginative adventures, but now stood as a symbol of their rivalry. Jake, the boy in the green tank top and blue shorts, tugged at the toy, his eyes narrowed in determined anger. Lucas, dressed in an orange shirt and green shorts, held on with equal resolve, his expression a mix of upset and determination. Their mother, Emily, was oblivious to the brewing storm, her hands busy with the dishes in the kitchen sink, the gentle hum of running water accompanying the silent battle behind her. The living room, with its soft sofa, small white dresser, and window adorned with pink curtains, was a picture of domestic tranquility, sharply contrasting the tension between the boys.

Suddenly, a sharp crack echoed through the room. The toy airplane, caught in the crossfire of the boys' tug-of-war, lay broken on the floor. Jake, now in a yellow shirt and blue shorts, stood in shock, his hands covering his eyes as tears began to flow. Lucas, in a green and yellow striped shirt, looked on in surprise and worry, his hand extended towards the broken toy as if trying to explain the accident. Emily, alerted by the noise and her sons' distress, stood with her hands on her hips, steam almost literally coming from her head. Her apron and green gloves dripped with soap suds, a testament to her interrupted chores. Her eyes flashed with frustration and concern as she took in the scene, her sons' argument finally reaching her ears and demanding her attention.

In the aftermath of the storm, a calm descended upon the house. Jake and Lucas, their argument forgotten, sat together at a round table, their heads bent over colorful sheets of paper. Jake, in his green sleeveless shirt with a white star, was all smiles as he shared his expertise in paper airplane crafting with Lucas. His friend, in an orange T-shirt, listened intently, his eyes wide with interest as he carefully folded a yellow sheet of paper. The table was a testament to their creativity, scattered with an array of completed paper airplanes in red, yellow, and purple. The room, with its cozy sofa, window dressed in cheerful curtains, and the warm sunlight streaming in, was a haven of peace and friendship.

The sound of laughter filled the living room as Jake and Lucas played with their new fleet of paper airplanes. Jake, in his green shirt and blue shorts, held a red airplane aloft, his eyes sparkling with joy and excitement. Lucas, in his orange shirt and light green shorts, laughed heartily, his eyes following the trajectory of the airplane as it soared through the air. The room was a whirlwind of color and motion, with paper airplanes scattered across the floor and table, a testament to the boys' boundless energy and imagination. Emily, standing at the entrance of the room, watched her sons with a smile on her face. The kitchen behind her, with its bottles and jars on the counter, was a picture of domestic warmth. The broken toy airplane was forgotten, replaced by the simple joy of childhood and the boundless potential of a sheet of paper.

</details>


