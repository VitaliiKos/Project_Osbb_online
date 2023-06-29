import {Outlet} from "react-router-dom";

import {Header} from "../../components";
import css from './mainLayout.module.css';
import {Footer} from "../../pages";

const MainLayout = () => {
    return (
        <div className={css.wrapper}>
            <div className={css.menu}>
                <Header/>
            </div>

            <div className={css.content}>
                <Outlet/>
            </div>

            <div className={css.footer}>
                <Footer/>
            </div>

        </div>
    );
};

export {MainLayout};