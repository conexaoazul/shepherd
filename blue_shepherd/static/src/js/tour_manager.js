/** @odoo-module */

import { registry } from "@web/core/registry";
import { Component, onWillStart, useEffect, useRef } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class TourManager extends Component {
    setup() {
        this.orm = useService("orm");
        this.actionService = useService("action");
        this.currentTour = null;

        onWillStart(async () => {
            await this.loadTours();
        });
    }

    async loadTours() {
        const tours = await this.orm.searchRead(
            "blue.shepherd.tour",
            [["active", "=", true]],
            ["name", "step_ids", "modal_overlay", "default_step_options", "exit_on_escape", "keyboard_navigation"]
        );

        tours.forEach(tour => this.initTour(tour));
    }

    async initTour(tourData) {
        const steps = await this.orm.searchRead(
            "blue.shepherd.step",
            [["tour_id", "=", tourData.id]],
            ["name", "title", "text", "element", "position", "scrollTo", "modalOverlayOpeningPadding",
             "show_cancel_link", "cancel_text", "next_text", "back_text", "extra_options"]
        );

        const tour = new Shepherd.Tour({
            useModalOverlay: tourData.modal_overlay,
            defaultStepOptions: tourData.default_step_options ? JSON.parse(tourData.default_step_options) : {},
            exitOnEsc: tourData.exit_on_escape,
            keyboardNavigation: tourData.keyboard_navigation,
        });

        steps.forEach(stepData => {
            const stepConfig = {
                title: stepData.title,
                text: stepData.text,
                attachTo: {
                    element: stepData.element,
                    on: stepData.position,
                },
                scrollTo: stepData.scrollTo,
                modalOverlayOpeningPadding: stepData.modalOverlayOpeningPadding,
                buttons: []
            };

            if (stepData.show_cancel_link) {
                stepConfig.buttons.push({
                    text: stepData.cancel_text || 'Skip',
                    action: tour.cancel,
                    classes: 'shepherd-button-secondary'
                });
            }

            if (steps.indexOf(stepData) > 0) {
                stepConfig.buttons.push({
                    text: stepData.back_text || 'Back',
                    action: tour.back,
                    classes: 'shepherd-button-secondary'
                });
            }

            if (steps.indexOf(stepData) < steps.length - 1) {
                stepConfig.buttons.push({
                    text: stepData.next_text || 'Next',
                    action: tour.next,
                    classes: 'shepherd-button-primary'
                });
            } else {
                stepConfig.buttons.push({
                    text: 'Finish',
                    action: tour.complete,
                    classes: 'shepherd-button-primary'
                });
            }

            if (stepData.extra_options) {
                Object.assign(stepConfig, JSON.parse(stepData.extra_options));
            }

            tour.addStep(stepConfig);
        });

        this.currentTour = tour;
    }

    startTour() {
        if (this.currentTour) {
            this.currentTour.start();
        }
    }
}

registry.category("main_components").add("TourManager", {
    Component: TourManager,
    props: { bus: null },
});