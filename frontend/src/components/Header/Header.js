import {NavLink} from "react-router-dom";

import {RouterEndpoints} from "../../routes";
import {UserInfoPage} from "../../pages";

const Header = () => {

    return (
        <>
            <NavLink to={''}>Головна</NavLink>
            <NavLink to={RouterEndpoints.osbb}>Наше ОСББ</NavLink>
            <NavLink to={RouterEndpoints.rent_and_services}>Оренда і послуги</NavLink>
            <NavLink to={RouterEndpoints.news_and_events}>Новини та події</NavLink>
            <NavLink to={RouterEndpoints.profile}>Особистий кабінет</NavLink>
            <NavLink to={RouterEndpoints.login}>Увійти</NavLink>
            <NavLink to={RouterEndpoints.register}>Зареєструватись</NavLink>
            <UserInfoPage/>
        </>
    );
};

export {Header};