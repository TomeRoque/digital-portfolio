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

        function showInfo(objectId) {
            const objectInfo = getObjectInfo(objectId);
            if (objectInfo) {
                infoContainer.innerHTML = `<p>Information about ${objectId} goes here.</p>`;
            }
        }

        function getObjectInfo(objectId) {
            // Replace this function with the logic to get the object's information
            // For now, we'll return some sample information based on the object's ID
            const objectInfoMap = {
                "object1": "This is information about Object 1.",
                "object2": "This is information about Object 2.",
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