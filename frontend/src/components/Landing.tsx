import './Landing.css';

const Landing = () => (
  <div className="landing-container">
    <div className="landing-left">
      <h1>Lorem ipsum</h1>
      <div className="landing-text">
        asdawdasdawdsdawdasdasd<br />
        awdasdasd<br />
        awdasdasdasdasdad
      </div>
    </div>
    <div className="landing-right">
      <svg width="220" height="220" viewBox="0 0 220 220" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="15" y="15" width="190" height="190" rx="20" stroke="#222" strokeWidth="6" fill="none"/>
        <circle cx="60" cy="60" r="16" stroke="#222" strokeWidth="6" fill="none"/>
        <polyline points="40,170 120,100 180,170" stroke="#222" strokeWidth="6" fill="none"/>
      </svg>
    </div>
  </div>
);

export default Landing; 