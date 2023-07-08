import React, {useEffect, useState} from 'react';
import {useDispatch, useSelector} from "react-redux";
import {useSearchParams} from "react-router-dom";

import {pollActions} from "../../redux";
import {Poll} from "../Poll/Poll";
import {PollForm} from "../PollForm/PollForm";
import css from './polls.module.css';

const Polls = () => {

    const [statusPoll, setStatusPoll] = useState(false);
    const dispatch = useDispatch();
    const {polls, errors} = useSelector(state => state.polls);
    const [query, setQuery] = useSearchParams({'page': '1'});

    useEffect(() => {
        dispatch(pollActions.getAll({'page': query.get('page')}))
    }, [])


    return (
        <div>
            <div>
                {!statusPoll &&
                    <div className={css.createPollBtn}>
                        <button onClick={() => setStatusPoll(true)}>Створити нове опитування</button>
                    </div>
                }
                {statusPoll &&
                    <div>
                        <PollForm setStatusPoll={setStatusPoll}/>
                    </div>
                }
            </div>
            {
                polls &&
                polls.map(poll => <Poll key={poll.id} poll={poll}/>)
            }

        </div>
    );
};

export {Polls};