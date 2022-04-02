import { Link } from "react-router-dom";

const Header = () => {
    return (
        <header className="flex justify-between items-center px-16">
            <h1 className="text-xl px-5">DaDay</h1>

            <nav>
                <ul className="flex py-4">
                    <li className="px-5"><Link to='/register'>Register</Link></li>
                    <li className="px-5"><Link to='/login'>Login</Link></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;