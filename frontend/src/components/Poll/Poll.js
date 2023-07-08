import React from 'react';
import {useDispatch} from "react-redux";

import {pollActions} from "../../redux";
import css from './css.module.css';

const Poll = ({poll}) => {

    const {id, question, description, choices, created_at} = poll;
    const dispatch = useDispatch();

    const selectVote = (voteId) => {
        console.log({id, 'choice': voteId})
        dispatch(pollActions.makeVote({id, 'choice': voteId}))
    }

    return (
        <div>
            <h3>Poll</h3>
            <div>
                <h2>{id}. {question}</h2>
                <h5>{description}</h5>

                <div className={css.choicesWrapper}>
                    {choices.map(choice =>
                        <div key={choice.id} className={css.pollChoice}>
                            <div>
                                <h4>{choice.id}. {choice['choice_text']} - {choice.percent}</h4>
                            </div>
                            <div>
                                <button onClick={() => selectVote(choice.id)}></button>
                            </div>
                        </div>
                    )}
                </div>
                <h4>{created_at}</h4>
            </div>

        </div>
    );
};

export {Poll};