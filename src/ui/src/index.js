import React from 'react';
import ReactDOM from 'react-dom';
import { groups } from 'lib/networking';

class Root extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            groups: []
        };
    }

    componentDidMount() {
    groups.list()
        .then(groups => {
            this.setState({
                    isLoaded: true,
                    groups: groups
                });
            },
            error => {
                this.setState({
                    isLoaded: true,
                    error: error
                });
            }
        )
    }

    render() {
        const { error, isLoaded, groups } = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (
                <ul>
                    {groups.map(group => (
                        <li key={group.id}>
                            {group.name}
                        </li>
                    ))}
                </ul>
            );
        }
    }
}

ReactDOM.render(
    <Root />,
    document.getElementById('root')
)