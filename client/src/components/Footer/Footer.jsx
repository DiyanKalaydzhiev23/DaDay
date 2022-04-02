const Footer = () => {
    return (
        <footer className="flex justify-between items-center px-16 text-2xl">
            <h1 className="text-xl px-5">DaDay</h1>

            <nav>
                <ul className="flex py-4">
                    <li className="px-5 nav-link"><a>Facebook</a></li>
                    <li className="px-5 nav-link"><a>LinkedIn</a></li>
                </ul>
            </nav>
        </footer>
    );
}

export default Footer;