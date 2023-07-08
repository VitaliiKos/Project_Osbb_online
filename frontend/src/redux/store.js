import {combineReducers, configureStore} from "@reduxjs/toolkit";

import {newsReducer, userReducer} from "./slice";
import {pollReducer} from "./slice";

const rootReducer = combineReducers({
    users: userReducer,
    news: newsReducer,
    polls: pollReducer,
});

const setupStore = () => configureStore({
    reducer: rootReducer
});

export {setupStore}