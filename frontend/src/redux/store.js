import {combineReducers, configureStore} from "@reduxjs/toolkit";

import {userReducer} from "./slice";

const rootReducer = combineReducers({
    users: userReducer,
});

const setupStore = () => configureStore({
    reducer: rootReducer
});

export {setupStore}