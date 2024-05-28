import React from 'react';
import '../styles/Projects.css';

const Projects = () => {
  const projectList = [
    {
      title: 'News Scraper App',
      description: 'Gather all of your news informations in one line',
      technologies: ['React', 'CSS', 'Python'],
      link: 'http://github.com/yourproject1'
    },
    {
      title: 'Personal Website',
      description: 'What you are looking at right now',
      technologies: ['JavaScript', 'HTML', 'React', 'FastAPI'],
      link: 'http://github.com/yourproject2'
    }
  ];

  return (
    <section id="projects">
      <h2>My Projects</h2>
      <div className="project-grid">
        {projectList.map((project, index) => (
          <div className="project-card" key={index}>
            <h3>{project.title}</h3>
            <p>{project.description}</p>
            <p><strong>Technologies:</strong> {project.technologies.join(', ')}</p>
            <a href={project.link} target="_blank" rel="noopener noreferrer">View Project</a>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Projects;
