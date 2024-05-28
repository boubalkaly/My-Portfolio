import React from 'react';
import '../styles/Header.css';

const Header = () => {
  return (
    <div >
    <header className='header'>
      <nav>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>
    </div>
  );
};

export default Header;