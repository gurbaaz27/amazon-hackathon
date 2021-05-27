
function randomNumber(min, max) { 
    return (Math.random() * (max - min) + min);
} 


async function getter(params,url)
{
    const response = await fetch(url,params);
    console.log(response);
    const label = await response.json();
    return label;

}

async function predictor()
{
    campaign_dict = {0:'Other',1:'Shoes Sale-Display Ads',2:'Seach Ads-Summer-Shoes',3:'Dynamic Search Ads-Shoes',4:'Father day shoes sale-Display ads'};
    device_category_dict = {0:'tablet',1:'desktop',2:'mobile'}
    social_network_dict = {0:'Other',1:'Facebook',2:'Instagram Stories',3:'Slashdot',4:'Twitter',5:'LinkedIn',6:'Yelp',7:'Quora'}
    var Data = {
         avg_session_duration : randomNumber(0,7000),
         campaign : 'Other',   // Some bug here, to be found and corrected
         hits : Math.floor(randomNumber(10,7600)),
         day_of_week : Math.floor(randomNumber(0,6)),
         day : Math.floor(randomNumber(1,31)),
         device_category : device_category_dict[Math.floor(randomNumber(0,2))],
         entrances : Math.floor(randomNumber(0,450)),
         events_per_session : randomNumber(0,400),
         exits : Math.floor(randomNumber(0,450)),
         hour : Math.floor(randomNumber(0,24)),
         organic_search : Math.floor(randomNumber(0,10)),
         page_depth : Math.floor(randomNumber(0,500)),
         page_views : Math.floor(randomNumber(1,5600)),
         page_views_per_session : randomNumber(1,450),
         sessions : Math.floor(randomNumber(1,450)),
         social_network : social_network_dict[Math.floor(randomNumber(0,7))],
         events : Math.floor(randomNumber(1,2000)),
         unique_events : Math.floor(randomNumber(1,600)),
         week : Math.floor(randomNumber(20,40)),
         frequency : Math.floor(randomNumber(1,20)),
    };
    console.log(Data);
  const url = 'https://cors-amazon.herokuapp.com/https://customer-classifier-app.herokuapp.com/predict';
  const params = {
      body:JSON.stringify(Data),
      // credentials: 'include',
      method:'POST',
      headers : {
        'Content-Type': 'text/plain',
      },
  }
  await getter(params,url).then(label => {
    preds = label['label']
    console.log(preds);
    document.getElementById("bn").click();
    if(preds == 'Window')
    document.getElementById("mypart").innerHTML = 'Congratulations! You have received a discount of flat 30%';
    else if(preds=='Buyer')
    document.getElementById("mypart").innerHTML = 'Congratulations! You have received a discount of flat 15%';
    else
    document.getElementById("mypart").innerHTML = 'Congratulations! You have received a discount of flat 50%';
  });

}

window.addEventListener('load', (event) => {
  predictor();
});