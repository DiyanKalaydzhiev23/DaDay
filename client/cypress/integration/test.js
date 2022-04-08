describe('Login page', () => {
    it('Login page loads', () => {
        cy.visit('/login');
        cy.get('#login-form').should('exist');
    });

    it('Login functionality works when entered correct username and password', () => {
        cy.visit('/login');

        cy.get('input[name=username]').type('mariana');
        cy.get('input[name="password"]').type('asdasd{enter}');

        cy.url().should('include', '/share-day');
        cy.get('nav').should('contain', 'Log out');
    });
});

describe('Logout', () => {
    it('Logout logs out the user', () => {
        cy.visit('/login');

        cy.get('input[name=username]').type('mariana');
        cy.get('input[name="password"]').type('asdasd{enter}');

        cy.wait(2000);
        cy.url().should('include', '/share-day');
        
        cy.get('nav').contains('Log out').click();
        cy.get('nav').should('contain', 'Login');
    })
});

describe('Share day', () => {
    it('Emotion selection loads on share day page', () => {
        cy.visit('/login');

        cy.get('input[name=username]').type('mariana');
        cy.get('input[name="password"]').type('asdasd{enter}');

        cy.wait(2000);
        cy.url().should('include', '/share-day');

        cy.get('.emotion-card').should('exist');
    });

    it('Emotion selection functionality works', () => {
        cy.visit('/login');

        cy.get('input[name=username]').type('mariana');
        cy.get('input[name="password"]').type('asdasd{enter}');

        cy.url().should('include', '/share-day');

        cy.get('.emotion-card').first().should('be.visible').click({force: true});

        cy.wait(2000);

        cy.get('#description-form').should('exist');
    });

    it('Note add works correctly', () => {
        cy.visit('/login');

        cy.get('input[name=username]').type('mariana');
        cy.get('input[name="password"]').type('asdasd{enter}');

        cy.url().should('include', '/share-day');

        cy.get('.emotion-card').first().should('be.visible').click({force: true});
        cy.get('#description-form textarea').should('exist');

        cy.get('#description-form textarea').type('test');
        cy.get('#description-form input').should('be.visible').click({force: true});

        cy.get('h1').should('contain', 'Thank you for your response! I\'d be glad to chat with you tomorrow too!');
    });
});

describe('All notes', () => {
    it('All notes works', () => {
        cy.visit('/login');

        cy.get('input[name=username]').type('mariana');
        cy.get('input[name="password"]').type('asdasd{enter}');

        cy.url().should('include', '/share-day');

        cy.visit('/notes/28');

        cy.get('.notes').should('contain', 'test');
    });
});

