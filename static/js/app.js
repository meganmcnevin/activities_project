interest_list = ['drawing', 'painting', 'paper craft', 'pottery', 'photography', 'knitting', 'sewing', 'water play', 'bubbles', 
    'camping', 'nature play', 'dress up', 'role play', 'puppets', 'dancing', 'singing', 'music', 'storytelling', 'baking', 'magic', 
    'experiments', 'programming', 'star gazing','active play', 'yoga']

const createDivsForChars = (word) => {
    for (const char of word) {
      const div = document.createElement('div');
      div.classList.add('letter-box');
      div.classList.add(char);
  
      document.querySelector('#word-container').append(div);
    }
  };