import { Link } from "react-router-dom";
import { useNavigate } from "react-router";

const Header = () => {
    const user = localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null;
    const navigate = useNavigate();
    
    const logout = () => {
        localStorage.removeItem('user');
        navigate('/login');
    }

    return (
        <header className="flex justify-between items-center px-16 text-2xl">
            <h1 className="text-xl px-5">DaDay</h1>

            <nav>
                {!user && 
                    <ul className="flex py-4">
                        <li className="px-5 nav-link"><Link to='/register'>Register</Link></li>
                        <li className="px-5 nav-link"><Link to='/login'>Login</Link></li>
                    </ul>
                }

                {user && 
                    <ul className="flex py-4">
                        <li className="px-5 nav-link" onClick={logout}>Log out</li>
                    </ul>
                }
            </nav>
        </header>
    );
}

export default Header;