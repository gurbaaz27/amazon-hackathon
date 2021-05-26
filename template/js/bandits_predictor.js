function randomNumber(min, max) { 
    return (Math.random() * (max - min) + min);
} 

async function gette(params,url)
{
    const response = await fetch(url,params);
    console.log(response);
    const label = await response.json();
    return label;

}


async function predict()
{
    location_dict = {0:'toronto, ontario, canada',1:'rochester, new york, usa',2:'fort myers, florida, usa',3:'wokingham, england, united kingdom',4:'millbrae, california, usa'}
    country_dict = {0:'usa',1:'canada',2:'other',3:'netherlands',4:'iran'}
    author_dict = {0:'Richard Bruce Wright',1:'Toni Morrison',2:'Michael Crichton',3:'Agatha Christie',4:'Frank E. Peretti'}
    public_dict = {0:1989,1:2002,2:2010,3:1994,4:2003}
    var Data = {
         Location : location_dict[Math.floor(randomNumber(0,4))],
         Age : randomNumber(0,100),
         Country : country_dict[Math.floor(randomNumber(0,4))],
         Book_Author : author_dict[Math.floor(randomNumber(0,4))],
         Year_Of_Publication : public_dict[Math.floor(randomNumber(0,4))]
    };
    console.log(Data);
  const url = 'https://cors-amazon.herokuapp.com/https://bandits-api.herokuapp.com/predict';
  const params = {
      body:JSON.stringify(Data),
      // credentials: 'include',
      method:'POST',
      headers : {
        'Content-Type': 'text/plain',
      },
  }
  await gette(params,url).then(label => {
      console.log(label.labels);
      document.getElementById("a").innerHTML=label.labels[0];
      document.getElementById("b").innerHTML=label.labels[1];
      document.getElementById("c").innerHTML=label.labels[2];
      document.getElementById("d").innerHTML=label.labels[3];
      document.getElementById("e").innerHTML=label.labels[4];
      document.getElementById("f").innerHTML=label.labels[5];
  });

}

window.addEventListener('load', (event) => {
    predict();
  });