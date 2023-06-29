import {Outlet} from "react-router-dom";

import {Header} from "../../components";
import {Footer} from "../../pages";
import css from './mainLayout.module.css';

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