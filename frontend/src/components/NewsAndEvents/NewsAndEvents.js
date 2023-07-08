import React from 'react';
import {useDispatch} from "react-redux";
import {newsActions} from "../../redux";

const NewsAndEvents = ({item}) => {
    const {id, title, body} = item;

    const dispatch = useDispatch();

    return (
        <div>
            <h3>NewsAndEvents</h3>
            <div>

                <h3>{id}. {title}</h3>
                <div>
                    <button onClick={() => dispatch(newsActions.setNewsForUpdate(item))}>Змінити</button>
                    <button onClick={() => dispatch(newsActions.deleteNews({id}))}>Видалити</button>
                </div>
            </div>
        </div>
    );
};

export {NewsAndEvents};