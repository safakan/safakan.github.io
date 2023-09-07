// This event ensures the script runs only after the HTML is fully loaded.
document.addEventListener('DOMContentLoaded', () => {
  
    // Handling mouseover and mouseout events
    const linkBoxes = document.querySelectorAll('.link-box');
    linkBoxes.forEach(linkBox => {
      linkBox.addEventListener('mouseover', () => {
        const title = linkBox.querySelector('.link-title');
        const description = linkBox.querySelector('.link-description');        
        title.style.display = 'none';  // Hide the title
        description.style.display = 'block';  // Show the description        
      });
      linkBox.addEventListener('mouseout', () => {
        const title = linkBox.querySelector('.link-title');
        const description = linkBox.querySelector('.link-description');        
        title.style.display = 'block'; // Show the title again
        description.style.display = 'none';  // Hide the description        

    });
    });
  
    // Replace image sources dynamically
    document.getElementById('business-box').querySelector('img').src = IMAGES.BUSINESS;
    document.getElementById('blog-box').querySelector('img').src = IMAGES.BLOG;
    document.getElementById('music-box').querySelector('img').src = IMAGES.MUSIC;
  });
  