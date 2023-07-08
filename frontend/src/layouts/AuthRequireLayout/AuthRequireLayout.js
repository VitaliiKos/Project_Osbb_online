import React from 'react';
import {Outlet} from "react-router-dom";

const AuthRequireLayout = () => {
    return (
        <div>
            <h3>AuthRequireLayout</h3>
            <Outlet/>
        </div>
    );
};

export {AuthRequireLayout};