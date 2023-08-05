//header scroll code
window.addEventListener('scroll', () => {
    const header = document.getElementById('main-header');
    if (window.scrollY === 0) {
      header.classList.remove('scrolled');
    } else {
      header.classList.add('scrolled');
    }
  });

//container change by click code
const infoContainer = document.getElementById("info");

const frameContainer = document.getElementById("frame");

        function showInfo(objectId) {
            const objectInfo = getObjectInfo(objectId);
            let imgSrc = null;
            if (objectInfo) {

            const allImages = document.querySelectorAll('.object-container img');
                allImages.forEach(image => {
                        if(image.id == 'career'){
                            image.src = `../../assets/static/portfolio/images/aboutIcons/carreira-notSelected.png`;
                        } else if(image.id == 'cumputing'){
                            image.src = `../../assets/static/portfolio/images/aboutIcons/uni-notSelected.png`;
                        } else if(image.id == 'editor'){
                            image.src = `../../assets/static/portfolio/images/aboutIcons/editor-notSelected.png`;
                        } else if(image.id == 'skills'){
                            image.src = `../../assets/static/portfolio/images/aboutIcons/skills-notSelected.png`;
                        }


                });

                if(objectId == 'object1'){
                    const objectImageElement = document.getElementById('career');
                    imgSrc = `../../assets/static/portfolio/images/aboutIcons/carreira.png`;
                    objectImageElement.src = imgSrc;
                    frame.src = `../../assets/templates/aboutPages/career.html`;
                } else if(objectId == 'object2'){
                    const objectImageElement = document.getElementById('cumputing');
                    imgSrc = `../../assets/static/portfolio/images/aboutIcons/uni.png`;
                    objectImageElement.src = imgSrc;
                    frame.src = `../../assets/templates/aboutPages/uni.html`;
                } else if(objectId == 'object3'){
                    const objectImageElement = document.getElementById('editor');
                    imgSrc = `../../assets/static/portfolio/images/aboutIcons/editor.png`;
                    objectImageElement.src = imgSrc;
                } else if(objectId == 'object4'){
                    const objectImageElement = document.getElementById('skills');
                    imgSrc = `../../assets/static/portfolio/images/aboutIcons/skills.png`;
                    objectImageElement.src = imgSrc;
                }

                var iframe = document.getElementById('info');
                iframe.style.display = 'block';
                iframe.scrollIntoView({ behavior: 'smooth' });



            }


        }

        function getObjectInfo(objectId) {
            // Replace this function with the logic to get the object's information
            // For now, we'll return some sample information based on the object's ID
            const objectInfoMap = {
                "object1": "This is information about Object 1.",
                "object2": "This is information about Object 2.",
                "object3": "This is information about Object 3.",
                "object4": "This is information about Object 4."
                // Add more object information as needed
            };

            return objectInfoMap[objectId];
        }

//dynamic age change
 // Replace 'YYYY-MM-DD' with your actual birthdate
        const birthday = '1998-08-29';

        function calculateAge(birthdate) {
            const birthdateArray = birthdate.split('-');
            const birthYear = parseInt(birthdateArray[0]);
            const birthMonth = parseInt(birthdateArray[1]);
            const birthDay = parseInt(birthdateArray[2]);

            const today = new Date();
            const currentYear = today.getFullYear();
            const currentMonth = today.getMonth() + 1; // Months are 0-indexed
            const currentDay = today.getDate();

            let age = currentYear - birthYear;

            // Check if the birthday has already occurred this year
            if (currentMonth < birthMonth || (currentMonth === birthMonth && currentDay < birthDay)) {
                age--;
            }

            return age;
        }

        const age = calculateAge(birthday);
        const dynamicParagraph = document.getElementById('age-paragraph');
        dynamicParagraph.textContent = `Hello, thank you for visiting my website! My name is Tomé Roque, and I am ${age} years old.`;