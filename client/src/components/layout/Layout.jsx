import Header from "../Header/Header";
import Footer from "../Footer/Footer";

const Layout = (props) => {
    return (
        <div> 
            <Header></Header>
            <main>{props.children}</main>
            <Footer></Footer>
        </div>
    );
}

export default Layout;